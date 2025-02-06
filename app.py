from flask import Flask, jsonify, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def speak():
    try:
        # Read text from file
        with open("Text.txt", "r") as file:
            text = file.read()

        # Convert text to speech
        speech = gTTS(text=text, lang='en', slow=False)
        speech.save("voice.mp3")

        # Serve the generated audio file
        return send_file("voice.mp3", as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
