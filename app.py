from flask import Flask, request
import whisper

app = Flask(__name__)

@app.route("/")
def home():
    return "RAPO AI READY"

@app.route("/audio", methods=["POST"])
def audio():

    data = request.data

    with open("voice.wav", "wb") as f:
        f.write(data)

    model = whisper.load_model("tiny")

    result = model.transcribe("voice.wav")

    return result["text"]

app.run(host="0.0.0.0", port=81)
