document.getElementById("faceAnalyzeForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const formData = new FormData();
  const fileInput = document.getElementById("faceImage");

  if (fileInput.files.length === 0) {
    alert("Silakan pilih file wajah dulu!");
    return;
  }

  formData.append("faceImage", fileInput.files[0]);

  fetch("http://localhost:5000/analyze-face", {
    method: "POST",
    body: formData
  })
    .then((res) => res.json())
    .then((data) => {
      console.log("Hasil analisis wajah:", data);
      alert("Hasil: " + data.result + " (Confidence: " + data.confidence + ")");
    })
    .catch((err) => {
      console.error("Error:", err);
      alert("Gagal mengirim gambar.");
    });
});
