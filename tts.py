from gtts import gTTS
import os
import re
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

# 🔹 आउटपुट फोल्डर की सेटिंग्स
OUTPUT_FOLDER = "tts_output"
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# 🔹 सुरक्षित फाइलनेम बनाने का फ़ंक्शन
def sanitize_text(text):
    """ टेक्स्ट को क्लीन करता है ताकि वह सुरक्षित और वैध हो """
    return re.sub(r"[^a-zA-Z0-9\s]", "", text).strip()

def text_to_speech(text, language="en"):
    """ 🔹 टेक्स्ट को स्पीच में बदलने का फ़ंक्शन """
    if not text or len(text.strip()) == 0:
        raise ValueError("Input text cannot be empty")

    clean_text = sanitize_text(text)
    tts = gTTS(text=clean_text, lang=language)

    filename = secure_filename(f"tts_{language}.mp3")
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    
    try:
        tts.save(file_path)
    except Exception as e:
        raise RuntimeError(f"Error saving TTS file: {str(e)}")

    return file_path

@app.route("/tts", methods=["POST"])
def tts_api():
    """ 🔹 टेक्स्ट को स्पीच में बदलने के लिए API """
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "Invalid request. 'text' is required"}), 400

    text = data["text"]
    language = data.get("language", "en")

    try:
        file_path = text_to_speech(text, language)
        return jsonify({"message": "TTS conversion successful", "file_url": f"/download/{os.path.basename(file_path)}"})
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except RuntimeError as re:
        return jsonify({"error": str(re)}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@app.route("/download/<filename>", methods=["GET"])
def download_tts(filename):
    """ 🔹 जेनेरेट की गई ऑडियो फ़ाइल डाउनलोड करने के लिए API """
    try:
        return send_file(os.path.join(OUTPUT_FOLDER, filename), as_attachment=True)
    except Exception as e:
        return jsonify({"error": f"File not found: {str(e)}"}), 404

@app.route("/")
def index():
    """ 🔹 होमपेज API """
    return jsonify({"message": "Welcome to AI-Transcriber TTS API"})

if __name__ == "__main__":
    app.run(debug=True)
