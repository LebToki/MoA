# Fix for Flask-Uploads compatibility with newer Werkzeug versions
import werkzeug
if not hasattr(werkzeug, 'secure_filename'):
    from werkzeug.utils import secure_filename as _secure_filename
    werkzeug.secure_filename = _secure_filename
if not hasattr(werkzeug, 'FileStorage'):
    from werkzeug.datastructures import FileStorage
    werkzeug.FileStorage = FileStorage

from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_migrate import Migrate
import os
import json
import traceback
import logging
from logging.handlers import RotatingFileHandler

# Ensure the 'uploads' directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Ensure the 'instance' directory exists for SQLite database
if not os.path.exists('instance'):
    os.makedirs('instance')

# Ensure the 'logs' directory exists for log files
if not os.path.exists('logs'):
    os.makedirs('logs')

from utils import generate_with_references, generate_together_stream
import config

app = Flask(__name__)

# Make branding config available to all templates
@app.context_processor
def inject_branding():
    return {
        'developer_name': config.DEVELOPER_NAME,
        'company_name': config.COMPANY_NAME,
        'company_url': config.COMPANY_URL,
        'github_username': config.GITHUB_USERNAME,
        'github_repo': config.GITHUB_REPO,
        'company_logo': config.COMPANY_LOGO,
        'app_name': config.APP_NAME,
        'app_description': config.APP_DESCRIPTION
    }
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24).hex())

# Use absolute path for SQLite database on Windows
instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)
db_path = os.path.join(instance_path, 'conversations.db')
# Convert Windows path to SQLite URI format (use forward slashes)
db_path_uri = db_path.replace('\\', '/')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path_uri}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_FILES_DEST'] = 'uploads'
app.config['UPLOADED_FILES_ALLOW'] = DOCUMENTS
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

db = SQLAlchemy(app)
migrate = Migrate(app, db)

files = UploadSet('files', DOCUMENTS)
configure_uploads(app, files)

# Configure logging
if not app.debug:
    # Create logs directory if it doesn't exist
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Set up file handler with rotation
    file_handler = RotatingFileHandler(
        os.path.join(log_dir, 'moa_app.log'),
        maxBytes=10240000,  # 10MB
        backupCount=10
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('MoA Chatbot application startup')


class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(200), nullable=False)
    messages = db.Column(db.Text, nullable=False, default='[]')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Conversation {self.id}: {self.topic}>'

    def to_dict(self):
        return {
            'id': self.id,
            'topic': self.topic,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


@app.route('/')
def home():
    try:
        conversations = Conversation.query.order_by(Conversation.updated_at.desc()).all()
        return render_template('index.html', conversations=conversations)
    except Exception as e:
        app.logger.error(f"Error in home route: {str(e)}")
        flash('An error occurred while loading conversations.', 'error')
        return render_template('index.html', conversations=[])


@app.route('/chat/<int:conv_id>', methods=['GET', 'POST'])
def chat(conv_id):
    try:
        conversation = Conversation.query.get_or_404(conv_id)
        conversations = Conversation.query.order_by(Conversation.updated_at.desc()).all()
        
        if request.method == 'POST':
            # Handle file upload
            instruction = None
            if 'file' in request.files:
                file = request.files['file']
                if file and file.filename:
                    try:
                        filename = secure_filename(file.filename)
                        if not filename:
                            flash('Invalid file name.', 'error')
                            return redirect(url_for('chat', conv_id=conv_id))
                        
                        file_path = os.path.join(app.config['UPLOADED_FILES_DEST'], filename)
                        file.save(file_path)
                        
                        # Process the uploaded file
                        content = extract_content(file_path)
                        if not content.strip():
                            flash('Could not extract content from the file.', 'error')
                            return redirect(url_for('chat', conv_id=conv_id))
                        
                        # Use custom instruction if provided, otherwise default
                        user_instruction = request.form.get('instruction', '').strip()
                        if user_instruction:
                            instruction = f"{user_instruction}\n\nDocument content:\n{content}"
                        else:
                            instruction = f"Please analyze and summarize the following document:\n\n{content}"
                        
                        # Clean up file after processing
                        try:
                            os.remove(file_path)
                        except Exception:
                            pass  # Ignore cleanup errors
                            
                    except Exception as e:
                        app.logger.error(f"Error processing file: {str(e)}")
                        flash(f'Error processing file: {str(e)}', 'error')
                        return redirect(url_for('chat', conv_id=conv_id))
            
            # Get instruction from form if not from file
            if not instruction:
                instruction = request.form.get('instruction', '').strip()
                if not instruction:
                    flash('Please provide an instruction or upload a file.', 'error')
                    return redirect(url_for('chat', conv_id=conv_id))
            
            # Get model parameters
            model = request.form.get('model', 'llama-3.1-70b-versatile')
            try:
                temperature = float(request.form.get('temperature', 0.7))
                temperature = max(0.0, min(2.0, temperature))  # Clamp between 0 and 2
            except (ValueError, TypeError):
                temperature = 0.7
            
            try:
                max_tokens = int(request.form.get('max_tokens', 2048))
                max_tokens = max(1, min(32768, max_tokens))  # Clamp between 1 and 32768
            except (ValueError, TypeError):
                max_tokens = 2048
            
            # Load messages safely
            try:
                messages = json.loads(conversation.messages) if conversation.messages else []
            except (json.JSONDecodeError, TypeError):
                messages = []
            
            # Add user message
            messages.append({"role": "user", "content": instruction})
            
            # Generate response
            try:
                output = generate_with_references(
                    model=model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    messages=messages,
                    references=[],
                    generate_fn=generate_together_stream,
                )
                
                final_output = ""
                for chunk in output:
                    if hasattr(chunk, 'choices') and chunk.choices:
                        delta = chunk.choices[0].delta
                        if hasattr(delta, 'content') and delta.content:
                            final_output += delta.content
                
                if not final_output.strip():
                    flash('No response generated. Please try again.', 'error')
                    return redirect(url_for('chat', conv_id=conv_id))
                
                # Add assistant response
                messages.append({"role": "assistant", "content": final_output})
                
                # Save to database
                conversation.messages = json.dumps(messages)
                conversation.updated_at = datetime.utcnow()
                db.session.commit()
                
            except Exception as e:
                app.logger.error(f"Error generating response: {str(e)}\n{traceback.format_exc()}")
                flash(f'Error generating response: {str(e)}', 'error')
                return redirect(url_for('chat', conv_id=conv_id))
            
            return redirect(url_for('chat', conv_id=conv_id))
        
        # GET request - display chat
        try:
            messages = json.loads(conversation.messages) if conversation.messages else []
        except (json.JSONDecodeError, TypeError):
            messages = []
        
        return render_template('chat.html', 
                             conversation=conversation, 
                             messages=messages, 
                             conversations=conversations)
    
    except Exception as e:
        app.logger.error(f"Error in chat route: {str(e)}\n{traceback.format_exc()}")
        flash('An error occurred.', 'error')
        return redirect(url_for('home'))


@app.route('/new', methods=['POST'])
def new_conversation():
    try:
        topic = request.form.get('topic', '').strip()
        if not topic:
            flash('Please provide a conversation topic.', 'error')
            return redirect(url_for('home'))
        
        # Limit topic length
        if len(topic) > 200:
            topic = topic[:200]
        
        new_conv = Conversation(topic=topic, messages='[]')
        db.session.add(new_conv)
        db.session.commit()
        
        return redirect(url_for('chat', conv_id=new_conv.id))
    
    except Exception as e:
        app.logger.error(f"Error creating conversation: {str(e)}")
        flash('Error creating conversation.', 'error')
        return redirect(url_for('home'))


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    try:
        db.drop_all()
        db.create_all()
        flash('All conversations have been reset.', 'info')
        return redirect(url_for('home'))
    except Exception as e:
        app.logger.error(f"Error resetting database: {str(e)}")
        flash('Error resetting conversations.', 'error')
        return redirect(url_for('home'))


def extract_content(file_path):
    """Extract text content from various file formats."""
    content = ""
    try:
        if file_path.endswith('.pdf'):
            import fitz  # PyMuPDF
            doc = fitz.open(file_path)
            for page in doc:
                content += page.get_text()
            doc.close()
        elif file_path.endswith('.docx'):
            import docx
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                content += para.text + "\n"
        elif file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            # Try to read as text file
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                pass
    except Exception as e:
        app.logger.error(f"Error extracting content from {file_path}: {str(e)}")
        raise
    
    return content


@app.errorhandler(404)
def not_found(error):
    flash('Page not found.', 'error')
    return redirect(url_for('home'))


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    app.logger.error(f"Internal server error: {str(error)}")
    flash('An internal error occurred.', 'error')
    return redirect(url_for('home'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
