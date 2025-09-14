# save as animate_audio_3d.py
import numpy as np
import librosa, librosa.feature
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import os
import subprocess

# ====== INPUT ======
AUDIO_PATH = "temp_audioampli.wav"     
OUT_MP4_NOAUDIO = "audio_3d_noaudio.mp4"
OUT_MP4_FINAL   = "audio_3d_with_audio.mp4"

# ====== PARAMETER FRAME ======
sr_target     = 22050
frame_length  = 2048
hop_length    = 512
min_freq_hz   = 0.0
max_freq_hz   = sr_target/2

# ====== LOAD ======
y, sr = librosa.load(AUDIO_PATH, sr=sr_target, mono=True)

# ====== FITUR PER FRAME ======
# Amplitudo pakai RMS
rms = librosa.feature.rms(
    y=y, frame_length=frame_length, hop_length=hop_length, center=True
)[0]

# Spectral centroid (Hz)
centroid = librosa.feature.spectral_centroid(
    y=y, sr=sr, n_fft=frame_length, hop_length=hop_length, center=True
)[0]

# Waktu per frame (detik)
times = librosa.frames_to_time(np.arange(len(rms)), sr=sr, hop_length=hop_length)

# (opsional) normalisasi/penyetelan sumbu agar enak dilihat
x_vals = rms                       
y_vals = np.clip(centroid, min_freq_hz, max_freq_hz)  
z_vals = times                     

# ====== SETUP FIGURE ======
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("Amplitude (RMS)")
ax.set_ylabel("Spectral Centroid (Hz)")
ax.set_zlabel("Time (s)")

# Biar skala tidak lompat-lompat
ax.set_xlim(0, x_vals.max()*1.05)
ax.set_ylim(0, max_freq_hz)
ax.set_zlim(0, z_vals.max())

# Color map setup (warna berdasar Y = centroid)
cmap = plt.get_cmap("plasma")
norm = plt.Normalize(vmin=min_freq_hz, vmax=max_freq_hz)

# Titik awal
scat = ax.scatter([], [], [], s=12, c='blue')


# ====== UPDATE FUNC ======
def update(frame_idx):
    idx = slice(0, frame_idx+1)
    X, Y, Z = x_vals[idx], y_vals[idx], z_vals[idx]

    # warna node berdasarkan centroid
    colors = cmap(norm(Y))

    scat._offsets3d = (X, Y, Z)
    scat.set_facecolor(colors)

    # rotasi kamera pelan ke kanan (ubah azim saja)
    elev, azim = 20, 30 + 0.05*frame_idx  # 0.2 derajat per frame
    ax.view_init(elev=elev, azim=azim)

    ax.set_title(f"3D Audio Features — frame {frame_idx+1}/{len(z_vals)}  t={z_vals[frame_idx]:.2f}s")
    return scat,

# ====== ANIMASI ======
fps = int(sr / hop_length)
anim = FuncAnimation(fig, update, frames=len(z_vals), interval=1000/fps, blit=False)

# Simpan video TANPA audio dulu
print("Rendering video (no audio)...")
anim.save(OUT_MP4_NOAUDIO, fps=fps, dpi=150)

plt.close(fig)

# ====== MUX AUDIO KE VIDEO ======
print("Muxing audio into video...")
subprocess.run([
    "ffmpeg", "-y",
    "-i", OUT_MP4_NOAUDIO,
    "-i", AUDIO_PATH,
    "-c:v", "copy", "-c:a", "aac", "-shortest",
    OUT_MP4_FINAL
], check=True)

print(f"Done! File jadi: {OUT_MP4_FINAL}")
