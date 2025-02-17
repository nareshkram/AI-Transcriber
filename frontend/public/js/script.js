document.addEventListener("DOMContentLoaded", function () {
    const uploadForm = document.getElementById("uploadForm");
    const fileInput = document.getElementById("audioFile");
    const resultDiv = document.getElementById("result");
    const loadingIndicator = document.getElementById("loading");

    uploadForm.addEventListener("submit", async function (event) {
        event.preventDefault();
        
        if (!fileInput.files.length) {
            alert("⚠️ कृपया एक ऑडियो फ़ाइल चुनें!");
            return;
        }

        loadingIndicator.style.display = "block";
        resultDiv.innerHTML = "";

        const formData = new FormData();
        formData.append("file", fileInput.files[0]); // `audioFile` से `file` में बदलें, जैसा कि Flask API में है

        try {
            // Flask API URL को localhost:5000 के साथ सेट करें
            const response = await fetch("http://localhost:5000/transcribe", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                throw new Error(`🚨 Server Error: ${response.statusText}`);
            }

            const data = await response.json();
            loadingIndicator.style.display = "none";
            resultDiv.innerHTML = `<h3>📄 Transcription Result:</h3><p>${data.transcription}</p>`;
        } catch (error) {
            loadingIndicator.style.display = "none";
            resultDiv.innerHTML = `<p style="color: red;">❌ ${error.message}</p>`;
            console.error("Error:", error);
        }
    });
});
