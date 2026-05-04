from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "RAPO SERVER LIVE"

@app.route("/audio", methods=["POST"])
def audio():
    data = request.data

    with open("voice.wav", "wb") as f:
        f.write(data)

    print("Audio received:", len(data))
    return "ok"

app.run(host="0.0.0.0", port=81)
