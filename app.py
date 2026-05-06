from flask import Flask, request
import speech_recognition as sr
from gtts import gTTS
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

        text = r.recognize_google(audio, language="en-IN").lower()

        print("USER:", text, flush=True)

        if "name" in text:
            reply = "I am Rapo"

        elif "hello" in text:
            reply = "Hello boss"

        elif "bye" in text:
            reply = "Goodbye boss"

        else:
            reply = "You said " + text

    except Exception as e:
        print(traceback.format_exc(), flush=True)
        reply = "I could not understand"

    tts = gTTS(reply, lang="en")
    tts.save("reply.mp3")

    print("REPLY:", reply, flush=True)

    return reply


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
