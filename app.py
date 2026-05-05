from flask import Flask, request
import speech_recognition as sr

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return "RAPO CHATBOT READY"


# ---------------- AUDIO CHAT ----------------
@app.route("/audio", methods=["POST"])
def audio():

    data = request.data

    # Save uploaded voice
    with open("voice.wav", "wb") as f:
        f.write(data)

    r = sr.Recognizer()

    try:
        with sr.AudioFile("voice.wav") as source:

            # Noise adjust
            r.adjust_for_ambient_noise(source, duration=0.2)

            # Read full audio
            audio_data = r.record(source)

        # Speech to text
        text = r.recognize_google(audio_data, language="en-US")

        text = text.lower()

        print("You said:", text)

        # ---------------- CHATBOT REPLIES ----------------
        if "hello" in text or "hi" in text:
            reply = "Hello boss"

        elif "how are you" in text:
            reply = "I am fine boss"

        elif "your name" in text or "who are you" in text:
            reply = "I am Rapo your robot friend"

        elif "time" in text:
            reply = "I do not have watch yet"

        elif "thank you" in text:
            reply = "Welcome boss"

        elif "bye" in text:
            reply = "Goodbye boss"

        else:
            reply = "I heard " + text

        print("Reply:", reply)

        return reply

    except sr.UnknownValueError:
        return "Could not understand"

    except sr.RequestError:
        return "Speech service error"

    except Exception as e:
        print(e)
        return "Server error"


# ---------------- TEXT CHAT (optional) ----------------
@app.route("/chat")
def chat():

    text = request.args.get("text", "").lower()

    if text == "":
        return "Say something"

    if "hello" in text:
        return "Hello boss"

    elif "how are you" in text:
        return "I am fine boss"

    elif "name" in text:
        return "I am Rapo"

    else:
        return "You said " + text


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
