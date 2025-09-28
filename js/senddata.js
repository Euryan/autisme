document.getElementById('autismForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const formData = new FormData(e.target);
  const jsonData = Object.fromEntries(formData.entries());

  console.log(jsonData); // Debug: pastikan data terbentuk

  fetch('http://localhost:5000/kirim-jawaban', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(jsonData)
  })
  .then(res => res.json())
  .then(data => {
    alert('Jawaban berhasil dikirim!');
    console.log(data);
  })
  .catch(err => {
    console.error('Gagal kirim:', err);
    alert('Gagal mengirim jawaban.');
  });
});