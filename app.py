from flask import Flask, request
import wave
import speech_recognition as sr

app = Flask(__name__)

@app.route("/")
def home():
    return "RAPO FREE AI READY"

@app.route("/audio", methods=["POST"])
def audio():

    data = request.data

    # save WAV
    with wave.open("voice.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(4)      # 32-bit
        wf.setframerate(16000)
        wf.writeframes(data)

    r = sr.Recognizer()

    with sr.AudioFile("voice.wav") as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
    except:
        text = "Could not understand"

    print(text)
    return text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
