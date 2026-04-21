from flask import Flask, request

app = Flask(__name__)

current_command = "s"

@app.route('/')
def home():
    return "Robot Server Running"

@app.route('/set')
def set_command():
    global current_command
    text = request.args.get('text', '').lower()

    if "forward" in text:
        current_command = "f"
    elif "back" in text:
        current_command = "b"
    elif "left" in text:
        current_command = "l"
    elif "right" in text:
        current_command = "r"
    elif "stop" in text:
        current_command = "s"

    return "Command set: " + current_command

@app.route('/get')
def get_command():
    return current_command

app.run(host='0.0.0.0', port=81)
