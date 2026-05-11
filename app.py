from flask import Flask, jsonify
import os

app = Flask(__name__)

# Data sementara (pura-puranya dari database)
tugas_list = [
    {"id": 1, "tugas": "Bikin kode Flask", "status": "Selesai"},
    {"id": 2, "tugas": "Deploy ke PaaS", "status": "Proses"}
]

# Endpoint 1: Beranda
@app.route('/')
def beranda():
    return jsonify({
        'pesan': 'API To-Do List Fahri Aktif',
        'versi': '1.0.0'
    })

# Endpoint 2: Lihat Daftar Tugas
@app.route('/tugas')
def lihat_tugas():
    return jsonify(tugas_list)

# Endpoint 3: Info Tambahan
@app.route('/info')
def info_api():
    return jsonify({
        'pembuat': 'Mohammad Fahri',
        'deskripsi': 'Tugas Mandiri PaaS Komputasi Awan'
    })

# Endpoint 4: Health Check (WAJIB DARI DOSEN)
@app.route('/health')
def cek_kesehatan():
    return jsonify({'status': 'sehat'})

if __name__ == '__main__':
    # Pakai port dari environment variable (Wajib buat PaaS)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)