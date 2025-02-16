from flask import Flask, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename

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

@app.route("/")
def index():
    """ 🔹 होमपेज API """
    return jsonify({"message": "Welcome to AI-Transcriber API"})

if __name__ == "__main__":
    app.run(debug=True)
