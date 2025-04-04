rom flask import Flask

app = Flask(_name_)

@app.route("/")
def hello():
    return "Привет! Сервер работает."

if name == "_main_":
    app.run(host='0.0.0.0', port=10000)
