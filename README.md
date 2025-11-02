# Proyek Dicoding Analisis Data: Bike Sharing

**by Fariz Husain Albar**  
*Follow Instagram: [@fariz.webdev](https://instagram.com/fariz.webdev)*

---

## 📋 Deskripsi Proyek

Alloo semuanyaaaa!  
Inii adalah proyek analisis data **Bike Sharing** yang saya kerjakan dalam rangka belajar analisis data dengan Python di Dicoding.  
Tujuan proyek ini adalah untuk mencari tahu **pola penyewaan sepeda**, **pengaruh faktor cuaca**, dan **perilaku pengguna sepeda** di berbagai musim dan jam.

Beberapa hal yang saya analisis:
- 📈 Tren penyewaan sepeda per musim  
- 🌦️ Pengaruh suhu, cuaca, dan kelembapan terhadap jumlah penyewaan  
- 📅 Perbandingan penggunaan antara hari kerja dan akhir pekan  

---

## Setup Environment

Pastikan kalian sudah menginstall **Miniconda / Anaconda** terlebih dahulu ya owkaii owkaii??  
Setelah itu, jalankan langkah-langkah berikut di **Anaconda Prompt** 👇

```bash
# Buat environment baru
conda create --name main-ds python=3.13

# Aktifkan environment
conda activate main-ds

# Install library utama untuk analisis data
pip install numpy pandas scipy matplotlib seaborn jupyter

# Install library tambahan untuk dashboard
pip install streamlit babel
```

Kalau semua sudah siap, tinggal jalankan dashboard-nya ajaa:
```bash
## Menjalankan Dashboard Streamlit
streamlit run dashboard/dashboard.py
```

## 📊 Insight Menarik

Beberapa hasil analisis yang ditemukan:
- Musim **semi dan panas** adalah periode paling sibuk untuk penyewaan sepedaa.  
- Puncak aktivitas pengguna terjadi di **jam 07.00 dan 17.00** (waktu berangkat dan pulang kerja).  
- **Suhu dan kelembapan** terbukti memengaruhi minat pengguna dalam menyewa sepeda.  

---

## Tentang Saya

Halo, saya **Fariz Husain Albar** — penggemar data dan web developmentt  
Saya suka mengubah data menjadi cerita yang bisa dipahami, baik lewat *dashboard interaktif* maupun *visualisasi data menarik*.  
  
Terima kasih temenn temennnn sudah mampir, jangan lupa kasih ⭐ di repo ini kalau kamu suka proyeknyaaa yaahhh!
