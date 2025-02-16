import React, { useState } from "react";

const UploadAudio = () => {
  const [file, setFile] = useState(null);
  const [transcription, setTranscription] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:5000/transcribe", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setTranscription(data.transcription || "Transcription failed.");
    } catch (error) {
      console.error("Error:", error);
      setTranscription("Error in transcription.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-container">
      <h2>Upload an Audio File</h2>
      <input type="file" accept=".mp3, .wav, .ogg" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Processing..." : "Upload & Transcribe"}
      </button>
      {transcription && <p><strong>Transcription:</strong> {transcription}</p>}
    </div>
  );
};

export default UploadAudio;
