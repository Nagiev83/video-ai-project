from flask import Flask, request, jsonify
import openai

app = Flask(__name__)


openai.api_key = "sk-ВОТ_СЮДА_ВСТАВЬ_ТВОЙ_КЛЮЧ"

@app.route("/")
def home():
    return "Привет! Сервер работает."

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_message = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # можно gpt-4 если есть доступ
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        ai_message = response['choices'][0]['message']['content']
        return jsonify({"reply": ai_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
