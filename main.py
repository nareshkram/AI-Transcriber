from flask import Flask, request, jsonify
from flask_cors import CORS
import whisper
import os

app = Flask(__name__)
CORS(app)

# Whisper मॉडल लोड करें (Tiny, Base, Small, Medium, या Large चुन सकते हैं)
model = whisper.load_model("base")

@app.route('/')
def home():
    return "AI Transcriber Server is Running!"

# API: ऑडियो फाइल को टेक्स्ट में कन्वर्ट करें
@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    file_path = os.path.join("uploads", audio_file.filename)
    
    # फाइल को सेव करें
    os.makedirs("uploads", exist_ok=True)
    audio_file.save(file_path)

    # ऑडियो फाइल ट्रांसक्राइब करें
    result = model.transcribe(file_path)
    
    # फाइल डिलीट कर दें (अगर ज़रूरी न हो)
    os.remove(file_path)

    return jsonify({'text': result['text']})

if __name__ == '__main__':
    app.run(debug=True)
