from flask import Flask, request, send_file
import speech_recognition as sr
from gtts import gTTS
import os
import traceback

app = Flask(__name__)

last_reply = "Hello boss"

# ---------------- HOME ----------------
@app.route("/")
def home():
    return "RAPO SERVER ONLINE"

# ---------------- AUDIO ----------------
@app.route("/audio", methods=["GET", "POST"])
def audio():
    global last_reply

    # Browser test
    if request.method == "GET":
        return "Audio endpoint ready. Use POST to send WAV."

    try:
        # Save uploaded audio
        with open("voice.wav", "wb") as f:
            f.write(request.data)

        r = sr.Recognizer()

        with sr.AudioFile("voice.wav") as source:
            audio_data = r.record(source)

        text = r.recognize_google(audio_data).lower()

        print("User said:", text)

        # ---------- Replies ----------
        if "hello" in text:
            last_reply = "Hello boss"

        elif "name" in text:
            last_reply = "I am Rapo"

        elif "how are you" in text:
            last_reply = "I am doing great boss"

        elif "bye" in text:
            last_reply = "Goodbye boss"

        else:
            last_reply = "You said " + text

    except Exception as e:
        print(traceback.format_exc())
        last_reply = "I could not understand"

    # Make MP3 every time
    tts = gTTS(text=last_reply, lang="en")
    tts.save("reply.mp3")

    return last_reply

# ---------------- MP3 REPLY ----------------
@app.route("/reply")
def reply():

    if os.path.exists("reply.mp3"):
        return send_file("reply.mp3", mimetype="audio/mpeg")

    # fallback
    tts = gTTS("Hello boss")
    tts.save("reply.mp3")
    return send_file("reply.mp3", mimetype="audio/mpeg")


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
