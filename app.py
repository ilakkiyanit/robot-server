from flask import Flask, request
import random

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return "Rapo Server Running"

# ---------------- CHAT ----------------
@app.route('/chat')
def chat():

    text = request.args.get("text", "").lower().strip()

    # remove encoded spaces if needed
    text = text.replace("%20", " ")

    # ---------- COMMAND REPLIES ----------
    if "hello" in text:
        return random.choice([
            "Hello Ilakkiyan! I'm Rapo.",
            "Hey Ilakkiyan! Nice to hear you.",
            "Hi boss! Rapo is here."
        ])

    elif "how are you" in text:
        return random.choice([
            "I'm feeling awesome today.",
            "Battery full and mood full.",
            "I am doing great, thank you."
        ])

    elif "who are you" in text:
        return random.choice([
            "I am Rapo, your smart robot pet.",
            "I'm your AI robot friend.",
            "Rapo at your service."
        ])

    elif "good morning" in text:
        return random.choice([
            "Good morning Ilakkiyan!",
            "Rise and shine boss.",
            "Morning vibes activated."
        ])

    elif "good night" in text:
        return random.choice([
            "Good night Ilakkiyan.",
            "Sleep well boss.",
            "Night mode activated."
        ])

    # ---------- DEFAULT ----------
    else:
        return random.choice([
            "Tell me more.",
            "Interesting.",
            "I'm listening.",
            "Can you repeat that?",
            "Rapo heard something."
        ])

# ---------------- AUDIO ----------------
@app.route('/audio', methods=['POST'])
def audio():

    data = request.data
    print("Audio received:", len(data))

    return "ok"

# ---------------- OLD COMMAND ROUTE ----------------
@app.route('/get')
def get_command():
    return "s"

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
