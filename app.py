from flask import Flask, request, jsonify
import openai

app = Flask(__name__)


openai.api_key = "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"

@app.route("/")
def hello():
    return "Привет! Сервер работает."

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_message = data.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    ai_message = response['choices'][0]['message']['content']
    return jsonify({"reply": ai_message})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
