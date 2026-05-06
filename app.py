from flask import Flask, request, send_file
import speech_recognition as sr
from gtts import gTTS
import os
import traceback

app = Flask(__name__)

@app.route("/")
def home():
    return "RAPO SERVER ONLINE"

@app.route("/audio", methods=["POST"])
def audio():

    try:
        with open("voice.wav","wb") as f:
            f.write(request.data)

        r = sr.Recognizer()

        with sr.AudioFile("voice.wav") as source:
            audio = r.record(source)

        text = r.recognize_google(audio).lower()

        print("USER:", text)

        if "name" in text:
            reply = "I am Rapo"

        elif "hello" in text:
            reply = "Hello boss"

        elif "bye" in text:
            reply = "Goodbye boss"

        else:
            reply = "You said " + text

        print("REPLY:", reply)

    except:
        reply = "I could not understand"

    tts = gTTS(reply)
    tts.save("reply.mp3")

    return reply


@app.route("/reply")
def reply():

    return send_file(
        "reply.mp3",
        mimetype="audio/mpeg",
        as_attachment=False,
        max_age=0
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
