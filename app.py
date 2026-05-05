from flask import Flask, request, send_file
app = Flask(__name__)

@app.route("/")
def home():
    return "RAPO AUDIO DEBUG"

@app.route("/audio", methods=["POST"])
def audio():
    data = request.data
    with open("voice.wav", "wb") as f:
        f.write(data)
    return "saved"

@app.route("/listen")
def listen():
    return send_file("voice.wav", mimetype="audio/wav")
