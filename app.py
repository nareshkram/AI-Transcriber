from flask import Flask, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename
import speech_recognition as sr  # स्पीच रिकॉग्निशन लाइब्रेरी
import os
import speech_recognition as sr
from pydub import AudioSegment


app = Flask(__name__)

# 🔹 1GB (1024MB) की मैक्सिमम फ़ाइल साइज़ लिमिट सेट करें
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024  # 1GB
app.config['UPLOAD_FOLDER'] = "uploads"

# 🔹 वैध ऑडियो फ़ाइल एक्सटेंशन्स
ALLOWED_EXTENSIONS = {"mp3", "wav", "ogg", "flac", "m4a"}

# 📌 सुनिश्चित करें कि अपलोड फ़ोल्डर मौजूद है
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    """ चेक करें कि फ़ाइल का एक्सटेंशन वैध है या नहीं """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def check_file_size(file):
    """ 📌 फाइल साइज 1GB से ज्यादा नहीं होनी चाहिए """
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)
    return file_size <= 1024 * 1024 * 1024  # 1GB

@app.route("/upload", methods=["POST"])
def upload_file():
    """ 🔹 फाइल अपलोड करने के लिए सुरक्षित API """
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type. Allowed formats: MP3, WAV, OGG, FLAC, M4A"}), 400

    if not check_file_size(file):
        return jsonify({"error": "File too large! Max allowed size is 1GB"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    try:
        file.save(file_path)
    except Exception as e:
        return jsonify({"error": f"File upload failed: {str(e)}"}), 500

    return jsonify({"message": "File uploaded successfully", "filename": filename})

@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    """ 🔹 अपलोड की गई फ़ाइल को डाउनलोड करने के लिए API """
    try:
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)
    except Exception as e:
        return jsonify({"error": f"File not found: {str(e)}"}), 404

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    """ 🔹 अपलोड की गई ऑडियो फाइल को ट्रांसक्राइब करें """
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file format"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    file.save(file_path)  # फाइल को सेव करें

    # 🎙️ **स्पीच रिकॉग्निशन का उपयोग करके ऑडियो को टेक्स्ट में बदलें**
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="en-US")
            return jsonify({"message": "Transcription successful", "text": text})
        except sr.UnknownValueError:
            return jsonify({"error": "Could not understand the audio"}), 400
        except sr.RequestError:
            return jsonify({"error": "Speech recognition service unavailable"}), 500

@app.route("/")
def index():
    """ 🔹 होमपेज API """
    return jsonify({"message": "Welcome to AI-Transcriber API"})

if __name__ == "__main__":
    app.run(debug=True)
def transcribe_audio(file_path):
    """ MP3 ऑडियो को टेक्स्ट में बदलें """
    recognizer = sr.Recognizer()

    # MP3 ऑडियो को WAV में कन्वर्ट करें (लेकिन फाइल सेव नहीं होगी)
    audio = AudioSegment.from_file(file_path, format="mp3")
    wav_path = file_path.replace(".mp3", ".wav")
    audio.export(wav_path, format="wav")

    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Error with the speech recognition service: {e}"
from pydub.utils import which  
import os  

# FFmpeg का पाथ सेट करें
os.environ["FFMPEG_BINARY"] = which("ffmpeg")
os.environ["FFPROBE_BINARY"] = which("ffprobe")
