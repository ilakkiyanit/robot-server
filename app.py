from flask import Flask, request
import speech_recognition as sr

app = Flask(__name__)

@app.route("/")
def home():
    return "RAPO FREE AI READY"

@app.route("/audio", methods=["POST"])
def audio():

    data = request.data

    with open("voice.wav", "wb") as f:
        f.write(data)

    r = sr.Recognizer()

    try:
        with sr.AudioFile("voice.wav") as source:

            r.adjust_for_ambient_noise(source, duration=0.2)

            audio_data = r.record(source)

        text = r.recognize_google(audio_data, language="en-US")

        print("You said:", text)

        return text

    except sr.UnknownValueError:
        return "Could not understand"

    except sr.RequestError:
        return "Speech service error"

    except Exception as e:
        print(e)
        return "Server error"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
