from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = "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"

# Function to check if a question is heatwave-related
def is_heatwave_related(question):
    # Add your logic here to determine if the question is heatwave-related
    # You can use simple keyword matching or more advanced NLP techniques
    # For this example, let's assume we have a list of heatwave-related keywords
    heatwave_keywords = ["heatwave",
    "high temperature",
    "extreme heat",
    "heat index",
    "heat advisory",
    "heat stress",
    "heat exhaustion",
    "heatstroke",
    "hot weather",
    "sweltering",
    "scorching",
    "sunburn",
    "dehydration",
    "hydration",
    "air conditioning",
    "fans",
    "sunscreen",
    "shade",
    "water consumption",
    "cooling centers", 
    "temperature",
    "spf",
    "heat emergency", 
    "climate",
    "climate change"]

    for keyword in heatwave_keywords:
        if keyword in question.lower():
            return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        if is_heatwave_related(question):
            response = openai.Completion.create(
                engine="text-davinci-002",  # Use the appropriate OpenAI engine for your needs
                prompt=question,
                max_tokens=150,
                stop=None,
            )
            answer = response.choices[0].text.strip()
            return render_template('index.html', question=question, answer=answer)
        else:
            return render_template('index.html', message="Please ask only heatwave-related questions.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)