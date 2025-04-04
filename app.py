
 from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Вставь сюда свой реальный OpenAI API ключ!
openai.api_key = "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"

@app.route("/")
def home():
    return "Привет! Сервер работает."

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_message = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Можно указать gpt-4, если у тебя есть доступ
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
