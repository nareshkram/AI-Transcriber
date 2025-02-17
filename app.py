from flask import Flask, request, jsonify
import speech_recognition as sr
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

@app.route('/')
def home():
    return "Flask Server is Running!"

@app.route('/transcribe', methods=['POST', 'OPTIONS'])
def transcribe_audio():
    if request.method == "OPTIONS":
        return jsonify({"message": "CORS Preflight Request"}), 200

    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    audio_file = request.files['file']
    audio_path = 'uploaded_audio.wav'
    audio_file.save(audio_path)

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language='hi-IN')
            response = json.dumps({'transcription': text}, ensure_ascii=False)
            return response, 200, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
