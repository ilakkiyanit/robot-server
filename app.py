from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "RAPO DEBUG READY"

@app.route("/audio", methods=["POST"])
def audio():
    data = request.data

    with open("voice.raw", "wb") as f:
        f.write(data)

    print("Received bytes:", len(data))

    return "UPLOAD OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
