from flask import Flask, request, send_file
import speech_recognition as sr
from gtts import gTTS
import traceback

app = Flask(__name__)

last_reply = "Rapo ready"

@app.route("/")
def home():
    return "RAPO SERVER ONLINE"

@app.route("/audio", methods=["GET","POST"])
def audio():

    global last_reply

    if request.method == "GET":
        return "OK"

    try:
        with open("voice.wav", "wb") as f:
            f.write(request.data)

        r = sr.Recognizer()

        with sr.AudioFile("voice.wav") as source:
            audio_data = r.record(source)

        text = r.recognize_google(audio_data)
        text = text.lower()

        print("\nUSER SAID:", text)

        # IMPORTANT DEBUG
        last_reply = "You said " + text

        if "hello" in text:
            last_reply = "Hello boss"

        elif "name" in text:
            last_reply = "I am Rapo"

        elif "bye" in text:
            last_reply = "Goodbye boss"

        print("REPLY:", last_reply)

        tts = gTTS(last_reply)
        tts.save("reply.mp3")

        return last_reply

    except Exception as e:
        print(traceback.format_exc())
        last_reply = "Could not understand"

        tts = gTTS(last_reply)
        tts.save("reply.mp3")

        return last_reply


@app.route("/reply")
def reply():
    return send_file("reply.mp3", mimetype="audio/mpeg")
