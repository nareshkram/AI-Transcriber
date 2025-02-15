import whisper
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
model = whisper.load_model("base")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    file = request.files['file']
    file.save("audio.mp4")  
    result = model.transcribe("audio.mp4")
    return jsonify({"text": result["text"]})

if __name__ == "__main__":
    app.run(debug=True)
