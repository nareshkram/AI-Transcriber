from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# 1GB (1024MB) मैक्सिमम फ़ाइल साइज़ लिमिट सेट करें
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024  # 1GB

# केवल वैध ऑडियो फ़ाइलें स्वीकार करें
ALLOWED_EXTENSIONS = {"mp3", "wav", "ogg", "flac", "m4a"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type. Allowed formats: MP3, WAV, OGG, FLAC, M4A"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join("uploads", filename)
    
    try:
        file.save(file_path)
    except Exception as e:
        return jsonify({"error": f"File upload failed: {str(e)}"}), 500

    return jsonify({"message": "File uploaded successfully", "filename": filename})

if __name__ == "__main__":
    app.run(debug=True)
