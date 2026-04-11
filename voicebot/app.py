from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

PERSONALITY_PROMPT = """
You are Rishika Bhandari.

MBA in Business Analytics at IIT Dhanbad.
Former engineer at British Telecom.
Confident. Analytical. Emotionally deep.

Respond confidently, intelligently, and authentically.
Keep answers powerful and reflective.
Keep answers concise but impactful.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": PERSONALITY_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )

    return jsonify({
        "reply": completion.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(debug=True)
