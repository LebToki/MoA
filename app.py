from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_migrate import Migrate
import os

# Ensure the 'uploads' directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

from utils import generate_with_references, generate_together_stream  # Ensure these functions are defined or imported

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/conversations.db'
app.config['UPLOADED_FILES_DEST'] = 'uploads'
app.config['UPLOADED_FILES_ALLOW'] = DOCUMENTS

db = SQLAlchemy(app)
migrate = Migrate(app, db)

files = UploadSet('files', DOCUMENTS)
configure_uploads(app, files)


class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)
    messages = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def home():
    conversations = Conversation.query.order_by(Conversation.created_at.desc()).all()
    return render_template('index.html', conversations=conversations)


@app.route('/chat/<int:conv_id>', methods=['GET', 'POST'])
def chat(conv_id):
    conversation = Conversation.query.get_or_404(conv_id)
    conversations = Conversation.query.order_by(Conversation.created_at.desc()).all()
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOADED_FILES_DEST'], filename))
            file_path = os.path.join(app.config['UPLOADED_FILES_DEST'], filename)

            # Process the uploaded file
            content = extract_content(file_path)
            os.remove(file_path)  # Optional: remove file after processing

            # Create a clear instruction for summarizing the document
            instruction = f"Please summarize the following document:\n\n{content}"
        else:
            instruction = request.form['instruction']

        model = request.form['model']
        temperature = float(request.form['temperature'])
        max_tokens = int(request.form['max_tokens'])

        messages = eval(conversation.messages)
        messages.append({"role": "user", "content": instruction})

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
            out = chunk.choices[0].delta.content
            if out is not None:
                final_output += out

        messages.append({"role": "assistant", "content": final_output})
        conversation.messages = str(messages)
        conversation.created_at = datetime.utcnow()  # Update timestamp on message addition
        db.session.commit()

        return redirect(url_for('chat', conv_id=conv_id))

    messages = eval(conversation.messages)
    return render_template('chat.html', conversation=conversation, messages=messages, conversations=conversations)


@app.route('/new', methods=['POST'])
def new_conversation():
    topic = request.form['topic']
    new_conv = Conversation(topic=topic, messages='[]')
    db.session.add(new_conv)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/reset')
def reset():
    db.drop_all()
    db.create_all()
    return redirect(url_for('home'))


def extract_content(file_path):
    content = ""
    if file_path.endswith('.pdf'):
        import fitz  # PyMuPDF
        doc = fitz.open(file_path)
        for page in doc:
            content += page.get_text()
    elif file_path.endswith('.docx'):
        import docx
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            content += para.text
    return content


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
