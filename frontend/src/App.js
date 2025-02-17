import React, { useState } from "react";
import axios from "axios";
import logo from "./logo.svg";
import "./App.css";

function App() {
  const [data, setData] = useState("");
  const [audioFile, setAudioFile] = useState(null);
  const [transcriptionStatus, setTranscriptionStatus] = useState("");

  // Fetch API से डेटा प्राप्त करना
  const fetchDataUsingFetch = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/transcribe", {
        method: "GET",
      });
      const result = await response.json();
      setData(result.message || "डेटा प्राप्त हुआ!");
    } catch (error) {
      console.error("Fetch API Error:", error);
      setData("Fetch API से डेटा लाने में त्रुटि हुई");
    }
  };

  // Axios से डेटा प्राप्त करना
  const fetchDataUsingAxios = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/transcribe");
      setData(response.data.message || "डेटा प्राप्त हुआ!");
    } catch (error) {
      console.error("Axios Error:", error);
      setData("Axios से डेटा लाने में त्रुटि हुई");
    }
  };

  // फाइल सेलेक्ट करने का हैंडलर
  const handleFileChange = (event) => {
    setAudioFile(event.target.files[0]);
  };

  // फाइल अपलोड और ट्रांसक्राइब करने का हैंडलर
  const handleFileUpload = async () => {
    if (!audioFile) {
      alert("कृपया एक ऑडियो फाइल सेलेक्ट करें।");
      return;
    }

    const formData = new FormData();
    formData.append("file", audioFile);

    try {
      const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const result = await response.json();
        setTranscriptionStatus("ट्रांसक्रिप्शन शुरू हो गया है...");
      } else {
        alert("फाइल अपलोड में समस्या आई");
      }
    } catch (error) {
      console.error("Error during file upload:", error);
      setTranscriptionStatus("फाइल अपलोड में त्रुटि हुई");
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>API से डेटा प्राप्त करने के लिए नीचे दिए गए बटन पर क्लिक करें:</p>
        <button onClick={fetchDataUsingFetch}>Fetch API से लाओ</button>
        <button onClick={fetchDataUsingAxios}>Axios से लाओ</button>

        <div className="mt-5">
          <input
            type="file"
            accept="audio/*"
            onChange={handleFileChange}
            className="mb-4 p-2 border rounded"
          />
          <button
            onClick={handleFileUpload}
            className="px-6 py-3 bg-blue-500 text-white rounded hover:bg-blue-700 transition"
          >
            Upload and Transcribe
          </button>
          {transcriptionStatus && (
            <div className="mt-4 p-4 bg-green-100 text-green-800 rounded">
              {transcriptionStatus}
            </div>
          )}
        </div>

        <p>📜 डेटा: {data}</p>
      </header>
    </div>
  );
}

export default App;
