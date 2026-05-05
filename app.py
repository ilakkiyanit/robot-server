from flask import Flask, request, send_file
import speech_recognition as sr
from gtts import gTTS

app = Flask(__name__)

last_reply = "Hello boss"

@app.route("/")
def home():
    return "RAPO TALK READY"

@app.route("/audio", methods=["POST"])
def audio():
    global last_reply

    data = request.data

    with open("voice.wav", "wb") as f:
        f.write(data)

    r = sr.Recognizer()

    try:
        with sr.AudioFile("voice.wav") as source:
            audio_data = r.record(source)

        text = r.recognize_google(audio_data).lower()

        if "hello" in text:
            last_reply = "Hello boss"

        elif "name" in text:
            last_reply = "I am Rapo"

        elif "bye" in text:
            last_reply = "Goodbye boss"

        else:
            last_reply = "You said " + text

        tts = gTTS(last_reply)
        tts.save("reply.mp3")

        return last_reply

    except:
        last_reply = "Could not understand"
        return last_reply

@app.route("/reply")
def reply():
    return send_file("reply.mp3", mimetype="audio/mpeg"
