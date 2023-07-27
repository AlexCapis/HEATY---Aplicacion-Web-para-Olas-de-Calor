from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Your OpenAI API key here
api_key = "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"
openai.api_key = api_key

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form["question"]
        answer = get_gpt_answer(question)
        return render_template("index.html", answer=answer)

    return render_template("index.html", answer=None)

def get_gpt_answer(question):
    # Use the OpenAI API to get the response
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the engine that suits your requirements
        prompt=question,
        max_tokens=300  # Adjust as needed
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)