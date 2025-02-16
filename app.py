import whisper
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS  # CORS इनेबल करने के लिए

app = Flask(__name__)
CORS(app)  # CORS को पूरे ऐप के लिए enable करें

# Whisper मॉडल लोड करें
model = whisper.load_model("base")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    file.save("audio.mp4")  # फाइल सेव करें
    
    # ट्रांसक्रिप्शन करें
    result = model.transcribe("audio.mp4")

    return jsonify({"text": result["text"]})

@app.route('/api/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file received"}), 400

    file = request.files['file']
    return jsonify({"message": "File received successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
