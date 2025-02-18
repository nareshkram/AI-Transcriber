document.getElementById("uploadForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    
    let formData = new FormData();
    let fileInput = document.getElementById("audioFile");
    if (fileInput.files.length === 0) {
        alert("कृपया एक ऑडियो फ़ाइल अपलोड करें");
        return;
    }
    
    formData.append("file", fileInput.files[0]);
    
    try {
        let response = await fetch("http://127.0.0.1:5000/transcribe", {
            method: "POST",
            body: formData
        });
        
        let result = await response.json();
        
        if (response.ok) {
            document.getElementById("transcriptionResult").innerText = "ट्रांसक्रिप्शन: " + result.transcription;
        } else {
            document.getElementById("transcriptionResult").innerText = "त्रुटि: " + result.error;
        }
    } catch (error) {
        console.error("Fetch Error:", error);
        document.getElementById("transcriptionResult").innerText = "सर्वर से कनेक्ट करने में समस्या हुई";
    }
});
