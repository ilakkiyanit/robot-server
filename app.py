from flask import Flask, request
import whisper

app = Flask(__name__)

model = whisper.load_model("base")

@app.route("/")
def home():
    return "RAPO AI READY"

@app.route("/audio", methods=["POST"])
def audio():

    data = request.data

    with open("voice.wav", "wb") as f:
        f.write(data)

    result = model.transcribe("voice.wav")

    text = result["text"]

    print("You said:", text)

    return text

app.run(host="0.0.0.0", port=81)
