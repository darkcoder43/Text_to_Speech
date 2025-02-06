# Flask Text-to-Speech Application

This is a simple Flask-based web application that converts text from a file into speech and serves it as an audio file (`.mp3`). It uses the [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) library for text-to-speech conversion and serves the resulting audio file through Flask.

## Features
- Reads text from a file (`Text.txt`).
- Converts text to speech using `gTTS`.
- Serves the generated `.mp3` audio file on a Flask route (`/speak`).
- Audio file can either be downloaded or streamed directly through the browser.

## Requirements
- Python 3.x
- Flask
- gTTS

### 1. Install required dependencies:

pip install Flask gTTS
### 2. Prepare the Text.txt file
Make sure you have a text file named Text.txt in the same directory where the app.py script is located. The script will read the contents of this file to convert the text into speech.

### 3. Running the Application
Run the Flask application:

python app.py
The application will start running on http://localhost:5000.
