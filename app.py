# =====================================================
# RAPO PET ROBOT - CLEAN SERVER CODE (Render / Flask)
# =====================================================

from flask import Flask, request, send_file
import speech_recognition as sr
from gtts import gTTS
import os
import traceback

app = Flask(__name__)

last_reply = "Rapo ready"

# =====================================================
# HOME
# =====================================================

@app.route("/")
def home():
    return "RAPO SERVER ONLINE"


# =====================================================
# AUDIO RECEIVE + RECOGNIZE
# =====================================================

@app.route("/audio", methods=["GET", "POST"])
def audio():

    global last_reply

    # browser test
    if request.method == "GET":
        return "Audio endpoint ready"

    try:
        # save incoming wav
        with open("voice.wav", "wb") as f:
            f.write(request.data)

        r = sr.Recognizer()
        r.energy_threshold = 300
        r.dynamic_energy_threshold = True

        with sr.AudioFile("voice.wav") as source:
            audio_data = r.record(source)

        # speech to text
        text = r.recognize_google(audio_data).lower()

        print("USER SAID:", text)

        # =================================================
        # COMMANDS
        # =================================================

        if "hello" in text or "hi" in text:
            last_reply = "Hello boss"

        elif "name" in text:
            last_reply = "I am Rapo"

        elif "how are you" in text:
            last_reply = "I am doing great boss"

        elif "bye" in text:
            last_reply = "Goodbye boss"

        elif "thank" in text:
            last_reply = "You are welcome boss"

        elif "time" in text:
            from datetime import datetime
            now = datetime.now().strftime("%I %M %p")
            last_reply = "The time is " + now

        else:
            last_reply = "You said " + text

    except Exception as e:
        print(traceback.format_exc())
        last_reply = "I could not understand"

    # =================================================
    # MAKE MP3
    # =================================================

    try:
        tts = gTTS(text=last_reply, lang="en")
        tts.save("reply.mp3")
    except:
        pass

    return last_reply


# =====================================================
# SPEAKER REPLY
# =====================================================

@app.route("/reply")
def reply():

    if os.path.exists("reply.mp3"):
        return send_file("reply.mp3", mimetype="audio/mpeg")

    tts = gTTS("Hello boss")
    tts.save("reply.mp3")

    return send_file("reply.mp3", mimetype="audio/mpeg")


# =====================================================
# RUN
# =====================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
