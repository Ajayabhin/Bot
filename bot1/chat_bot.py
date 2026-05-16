from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import os

load_dotenv("../.env")

app = Flask(__name__)



client = InferenceClient(
    provider="fireworks-ai",
    api_key=os.getenv("CHATBOT_API_KEY")
)

@app.route("/")
def home():
    return render_template("template.html")

@app.route("/chat", methods=["POST"])
def chat():

    try:
         
        user_message = request.json["message"]

        response = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[
                {   
                    "role": "user", 
                    "content": user_message}
            ],            
            max_tokens=100
        )

        #bot_reply = response  # returns a string dir
       
        # response = client.chat.completions.create(
        #     model="gpt-4.1-mini",
        #     messages=[
        #         {
        #             "role": "user",
        #             "content": user_message
        #         }
        #     ]
        # )

        bot_reply = response.choices[0].message.content

        return jsonify({
            "reply": bot_reply
        })

    except Exception as e:

        return jsonify({
            "reply": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)
# print("hello")