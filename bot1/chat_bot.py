from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os

load_dotenv("../.env")

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return render_template("template.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
# print("hello")