from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Server Running"

@app.route('/audio', methods=['POST'])
def audio():
    data = request.data

    print("Audio received:", len(data))

    return "ok"

@app.route('/get')
def get_command():
    return "s"

app.run(host='0.0.0.0', port=81)
