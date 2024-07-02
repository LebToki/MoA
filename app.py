from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from utils import generate_with_references, generate_together_stream
from flask_session import Session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conversations.db'
db = SQLAlchemy(app)
Session(app)

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)
    messages = db.Column(db.Text, nullable=False)

@app.route('/')
def home():
    conversations = Conversation.query.all()
    return render_template('index.html', conversations=conversations)

@app.route('/chat/<int:conv_id>', methods=['GET', 'POST'])
def chat(conv_id):
    conversation = Conversation.query.get_or_404(conv_id)
    conversations = Conversation.query.all()  # Fetch all conversations for the sidebar
    if request.method == 'POST':
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

        # Format the output as a list if it starts with "Here are"
        if final_output.startswith("Here are"):
            final_output = "<ul>" + "".join([f"<li>{item}</li>" for item in final_output.split("\n")]) + "</ul>"

        messages.append({"role": "assistant", "content": final_output})
        conversation.messages = str(messages)
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

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
