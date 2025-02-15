async function processVideo() {
    let fileInput = document.getElementById('videoUpload');
    if (fileInput.files.length === 0) {
        alert("Please upload a video file first.");
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput.files[0]);

    let response = await fetch("/transcribe", {
        method: "POST",
        body: formData
    });

    let data = await response.json();
    document.getElementById('result').innerText = data.text;
}
