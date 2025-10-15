## 🏙️ Data Kelurahan – Project Django

### 👨‍🎓 Identitas Mahasiswa  
- **Nama:** Imam Untung Solihin  
- **NIM:** 23201016  
- **Mata Kuliah:** Framework Programming  

---

### 📘 Deskripsi Project
Proyek ini merupakan aplikasi berbasis **Django** yang digunakan untuk mengelola data warga dan pengaduan di tingkat kelurahan.  
Aplikasi ini dikembangkan sebagai bagian dari tugas mata kuliah Framework Programming.  

---

### ⚙️ Fitur Utama
- 📋 Menampilkan daftar warga  
- 🔍 Melihat detail informasi warga  
- 📨 Menampilkan daftar pengaduan warga  
- 💾 Penyimpanan data menggunakan database SQLite  

---

### 🧩 Struktur Direktori
```
kelurahan/
│
├── kelurahan/         # Folder utama konfigurasi Django
│   ├── settings.py    # Pengaturan utama proyek
│   ├── urls.py        # Routing utama
│   └── wsgi.py
│
├── warga/             # Aplikasi utama
│   ├── models.py      # Struktur data (database)
│   ├── views.py       # Logika tampilan
│   ├── urls.py        # Routing halaman warga
│   └── templates/     # Template HTML (antarmuka)
│
└── db.sqlite3         # Database proyek
```

---

### 🚀 Cara Menjalankan Proyek
1. Buka terminal dan masuk ke direktori proyek  
   ```bash
   cd Djangi/kelurahan
   ```

2. Jalankan server lokal Django  
   ```bash
   python manage.py runserver
   ```

3. Buka browser dan akses:  
   👉 `http://127.0.0.1:8000/`

---

### 💡 Catatan Tambahan
- Pastikan virtual environment aktif sebelum menjalankan proyek.  
- File ini akan membantu memahami isi proyek dengan cepat.  
