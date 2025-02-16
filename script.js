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
document.getElementById("uploadButton").addEventListener("click", function() {
    let fileInput = document.getElementById("fileInput");
    let formData = new FormData();
    formData.append("file", fileInput.files[0]);

    fetch("http://127.0.0.1:5000/api/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error("Error:", error));
});
