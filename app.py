from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Robot Server Running"

@app.route('/command')
def command():
    text = request.args.get('text', '').lower()

    if "forward" in text:
        return "f"
    elif "back" in text:
        return "b"
    elif "left" in text:
        return "l"
    elif "right" in text:
        return "r"
    elif "stop" in text:
        return "s"
    else:
        return "s"

if __name__ == "__main__":
    app.run()
