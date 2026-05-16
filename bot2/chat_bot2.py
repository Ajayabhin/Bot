from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import requests
import os

load_dotenv("../.env")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("template.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json["message"]

        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "llama3.2",
                "messages": [
                    {"role": "user", "content": user_message}
                ],
                "stream": False
            }
        )

        bot_reply = response.json()["message"]["content"]
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"reply": str(e)})

if __name__ == "__main__":
    app.run(debug=True)