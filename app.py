from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Rapo Server Running"

@app.route('/chat')
def chat():
    text = request.args.get("text","").lower()

    if "hello" in text:
        return "Hello Ilakkiyan! I'm Rapo."
    elif "how are you" in text:
        return "I'm feeling awesome today."
    elif "who are you" in text:
        return "I'm your robot pet."
    else:
        replies = [
            "Tell me more.",
            "Interesting.",
            "I'm listening.",
            "Say that again."
        ]
        return random.choice(replies)

@app.route('/get')
def get_command():
    return "s"

@app.route('/audio', methods=['POST'])
def audio():
    data = request.data
    print("Audio received:", len(data))
    return "ok"

app.run(host='0.0.0.0', port=81)
