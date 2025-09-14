# 🎶 3D Audio Visualization (SmartAIoT Project)

<p align="center">
  <img src="assets/smartiot.png" alt="SmartAIoT Logo" width="200"/>
</p>

Proyek ini merupakan bagian dari **SmartAIoT**, yang berfokus pada solusi berbasis **Artificial Intelligence of Things (AIoT)**.  
Dalam proyek ini, audio divisualisasikan dalam ruang 3D sehingga menghasilkan animasi dinamis yang menyajikan **hubungan antara amplitudo, frekuensi, dan waktu**.  

👉 Ikuti kami di Instagram: [@solusipintar.aiot](https://www.instagram.com/solusipintar.aiot/)

---

## 📂 Struktur Folder
```
SmartAIoT/
└── 3D audio visualization/
    ├── animate_audio_3d.py        # script utama
    ├── requirements.txt           # dependencies Python
    ├── temp_audio.wav             # contoh audio
    ├── temp_audioampli.wav        # contoh audio lain
    ├── audio_3d_noaudio.mp4       # contoh hasil video (tanpa audio)
    └── audio_3d_with_audio.mp4    # contoh hasil video (dengan audio)
```

---

## ⚡ Instalasi

1. Clone repository:
   ```bash
   git clone https://github.com/<username>/SmartAIoT.git
   cd SmartAIoT/"3D audio visualization"
   ```

2. (Opsional) Buat virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate     # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Pastikan **FFmpeg** sudah terinstall dan ada di `PATH`.  
   - Windows (via Chocolatey):
     ```bash
     choco install ffmpeg -y
     ```
   - Linux (Debian/Ubuntu):
     ```bash
     sudo apt install ffmpeg
     ```
   - Mac:
     ```bash
     brew install ffmpeg
     ```

---

## ▶️ Menjalankan Script

1. Simpan audio yang ingin divisualisasikan ke dalam folder project (misalnya `temp_audioampli.wav`).  
2. Jalankan script:

   ```bash
   python animate_audio_3d.py
   ```

3. Script akan menghasilkan:
   - `audio_3d_noaudio.mp4` → video animasi tanpa audio  
   - `audio_3d_with_audio.mp4` → video animasi dengan audio asli  

---

## 🎨 Visualisasi
- **X-axis** → Amplitude (RMS)  
- **Y-axis** → Spectral Centroid (Hz)  
- **Z-axis** → Time (s)  
- **Color** → Frequency band (colormap plasma)  
- Node baru muncul berwarna terang, node lama tetap ada dengan transparansi menurun → membentuk efek “bintang”  

---

## 📌 Catatan
- File audio besar (`.mp3`, `.wav`, `.mp4`) sebaiknya **tidak diupload** ke GitHub (gunakan `.gitignore`).  
- Script bisa dikembangkan lebih lanjut untuk menambahkan efek fade-out atau variasi kamera.  

---

## 📜 Lisensi
MIT License © 2025 SmartAIoT
