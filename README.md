# AI_Data_Process

Kumpulan tugas dari Pelatihan **Artificial Intelligence for Data Process** (Sesi 1–3, 10-11 November 2026). Seluruh tugas berjalan di **Python & Google Colab** dengan **data sintetis** untuk latihan, bukan data pelanggan nyata.

Alurnya menyambung dari data sampai perawatan: **data tepercaya → solusi terintegrasi → solusi yang dipantau dan dirawat.**

| Tugas | Unit kompetensi | Inti pekerjaan |
|---|---|---|
| [Tugas 1](tugas-1-data) | UK 1 Memasukkan Data · UK 2 Memvalidasi Data | Membaca CSV, memeriksa dengan 6 aturan, memisahkan data bersih, karantina, dan disisihkan |
| [Tugas 2](tugas-2-integrasi) | UK 3 Mengintegrasikan Komponen · UK 4 Memasang Solusi AI | Membangun pipeline model churn, menyimpan model, membuat fungsi prediksi dan form Gradio |
| [Tugas 3](tugas-3-perawatan) | UK 5 Merencanakan Perawatan · UK 6 Merawat Solusi AI | Menyusun rencana perawatan, memantau batch data baru, mencatat dan menutup insiden |

---

## Tugas 1 — Pemasukan dan Validasi Data

**UK 1:** file CSV diterima apa adanya (ukuran dan SHA-256 dicatat), dibaca menjadi tabel, dicek bentuk dan tipenya, lalu disalin tanpa menimpa file sumber.
**UK 2:** format dirapikan, enam pemeriksaan dijalankan (kosong, ID kembar, umur 18–100, kontrak Monthly/Annual, tagihan tidak negatif, churn Yes/No), lalu tiap baris diputuskan nasibnya. Data bermasalah **dikarantina, bukan dihapus**.

| Hasil dari 20 baris | Jumlah |
|---|---|
| Bersih (`data_pelanggan_bersih.csv`) | 10 |
| Dikarantina (`data_karantina.csv`) | 9 |
| Disisihkan (salinan persis C0015) | 1 |
| Temuan di `catatan_validasi.csv` | 12 (9 karantina, 1 disisihkan, 2 diperbaiki) |

Rekonsiliasi: 10 + 9 + 1 = 20, tidak ada data yang hilang.

## Tugas 2 — Integrasi dan Pemasangan Solusi AI

Model prediksi churn sederhana pada dataset sintetis 160 baris:
- Input 5 fitur (`age`, `contract`, `monthly_charge`, `tenure_months`, `support_calls`); `customer_id` tidak ikut.
- Data dibagi 128 latih dan 32 uji.
- Pipeline: `StandardScaler` + `OneHotEncoder` + `LogisticRegression`. Akurasi uji sekitar **0,78**.
- Model disimpan dengan `joblib` bersama metadata JSON, lalu dihubungkan ke fungsi `predict_churn` dan form **Gradio**.
- Bukti pemasangan: `requirements_hari2_terpasang.txt` dan `app_hari2.py`.

> Jangan memuat file `.joblib` dari sumber yang tidak dipercaya. Tautan share Gradio bersifat publik dan sementara, jadi jangan isi data asli.

## Tugas 3 — Perencanaan dan Perawatan Solusi AI

- **Rencana perawatan** tujuh area: artefak, kualitas data, pergeseran data, stabilitas prediksi, kinerja model, lingkungan, dan insiden.
- **Monitoring** dengan baseline 160 baris dan tiga batch baru (80 baris):

| Batch | Status | Baris valid |
|---|---|---|
| Normal | HIJAU | 80 / 80 |
| Bermasalah | MERAH | 60 / 80 (kosong 5%, tidak valid 25%, kategori `Weekly` 6) |
| Perbaikan | HIJAU | 80 / 80 |

- **Insiden** `INC-H3-001`: batch bermasalah dikarantina, data tidak diubah diam-diam, dan insiden ditutup dengan bukti sebelum dan sesudah.
- Ambang pada notebook adalah **aturan latihan**, bukan standar universal.

---

## Struktur Repositori

```
workshop-ai-data-process/
├── README.md
├── data/
│   └── data_pelanggan_latihan.csv
├── tugas-1-data/
│   ├── Tugas1.ipynb
│   ├── Tugas1_Presentasi_Script.pdf
│   ├── data_pelanggan_bersih.csv
│   ├── data_karantina.csv
│   └── catatan_validasi.csv
├── tugas-2-integrasi/
│   ├── Tugas2.ipynb
│   ├── Tugas2_Presentasi_Script.pdf
│   ├── app_hari2.py
│   ├── requirements_hari2_terpasang.txt
│   ├── metadata_model_hari2.json
│   └── model_churn_hari2.joblib
└── tugas-3-perawatan/
    ├── Tugas3.ipynb
    ├── Tugas3_Presentasi_Script.pdf
    ├── rencana_perawatan_hari3_terisi.csv
    ├── laporan_monitoring_hari3.csv
    ├── laporan_monitoring_hari3.json
    ├── log_insiden_hari3_terisi.csv
    └── grafik_monitoring_hari3.png
```

## Cara Menjalankan

1. Buka [Google Colab](https://colab.research.google.com), pilih **File → Upload notebook**, lalu unggah notebook tugas yang diinginkan.
2. Jalankan sel dari atas ke bawah. Saat diminta, unggah dataset yang dibutuhkan.
3. Cocokkan hasilnya dengan angka pada ringkasan di atas.

Kebutuhan dataset:
- **Tugas 1:** `data/data_pelanggan_latihan.csv`.
- **Tugas 2 dan 3:** memakai dataset dan berkas kit dari penyelenggara workshop (tidak disertakan di repositori ini).
- **Tugas 3:** instal library dengan versi terkunci dari `requirements_hari3.txt` (pandas 3.0.3, numpy 2.5.1, scikit-learn 1.9.0, joblib 1.5.3, matplotlib 3.10.8). Model hanya dimuat jika versi scikit-learn di metadata sama dengan versi runtime.

## Teknologi

Python 3 · pandas · NumPy · scikit-learn · joblib · Gradio · Matplotlib · Google Colab

## Kredit

Materi, data latihan, dan template berasal dari penyelenggara workshop. Seluruh data bersifat sintetis.

## Penulis

**Evelyn Anastasia**
