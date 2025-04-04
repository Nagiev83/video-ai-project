from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

PYXL_API_KEY = "pxl_live_rVt123pXfLQzj0aBCx45FgYtHkPzNaMZ"

@app.route("/")
def hello():
    return "Привет! Сервер работает на Pyxl.Pro."

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_message = data.get("message", "")

    response = requests.post(
        "https://api.pyxl.pro/v1/chat/completions",
        headers={"Authorization": f"Bearer {PYXL_API_KEY}"},
        json={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": user_message}]
        }
    )

    response_data = response.json()
    ai_message = response_data['choices'][0]['message']['content']

    return jsonify({"reply": ai_message})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
