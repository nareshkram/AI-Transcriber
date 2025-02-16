from flask import Flask, request, jsonify
import speech_recognition as sr
import json
from flask_cors import CORS  # ✅ React से API कॉल करने के लिए CORS इनेबल किया

app = Flask(__name__)
CORS(app)  # ✅ CORS इनेबल किया

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    audio_file = request.files['file']
    audio_path = 'uploaded_audio.wav'
    audio_file.save(audio_path)

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language='hi-IN')  # ✅ हिंदी ट्रांसक्रिप्शन
            
            # 🔹 ensure_ascii=False जोड़ा ताकि हिंदी टेक्स्ट सही दिखे
            response = json.dumps({'transcription': text}, ensure_ascii=False)
            return response, 200, {'Content-Type': 'application/json; charset=utf-8'}
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
