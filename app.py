from flask import Flask, request, render_template
from utils import generate_with_references, generate_together_stream

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    instruction = request.form['instruction']
    model = request.form['model']
    temperature = float(request.form['temperature'])
    max_tokens = int(request.form['max_tokens'])

    data = {
        "instruction": [[{"role": "user", "content": instruction}]],
        "references": [""],
        "model": [model],
    }

    output = generate_with_references(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        messages=data["instruction"][0],
        references=data["references"],
        generate_fn=generate_together_stream,
    )

    final_output = ""
    for chunk in output:
        out = chunk.choices[0].delta.content
        if out is not None:
            final_output += out

    return render_template('index.html', output=final_output)

if __name__ == "__main__":
    app.run(debug=True)
