# Customer Data Validation: Memasukkan & Memvalidasi Data Pelanggan

Pipeline sederhana dengan **Python & pandas** untuk memasukkan data pelanggan dari file CSV, memeriksanya dengan enam aturan validasi, memisahkan data **valid** dan **karantina**, lalu menyusun **laporan kualitas data**.

Proyek ini dikerjakan sebagai hasil latihan pada workshop *Artificial Intelligence for Data Process* (Sesi 1, 10 November 2026), mencakup dua tahap:

| Tahap | Tujuan |
|---|---|
| **UK 1 — Memasukkan Data** | Menerima file CSV, membacanya sebagai tabel, memeriksa bentuk dan tipe data, lalu menyimpan salinan tanpa mengubah file sumber |
| **UK 2 — Memvalidasi Data** | Merapikan teks dan angka, menjalankan 6 pemeriksaan, memisahkan data valid dan karantina, lalu menyusun laporan kualitas |

> **Catatan:** data yang dipakai adalah **data sintetis untuk latihan** (bukan data pelanggan nyata). Materi dan data latihan berasal dari penyelenggara workshop.

---

## Alur Kerja

```
data_pelanggan_latihan.csv
        │
        ▼
 [UK 1] Terima & catat berkas → baca sebagai tabel → cek bentuk/kolom/tipe → simpan salinan
        │
        ▼
 01_data_hasil_pemasukan.csv
        │
        ▼
 [UK 2] Rapikan data → 6 pemeriksaan → pisahkan valid / karantina → laporan kualitas
        │
        ├── Data Valid.xlsx
        ├── Data Karantina.xlsx
        └── Laporan Kualitas.xlsx
```

Prinsip utamanya: **data bermasalah tidak dihapus**. Baris yang gagal dipindah ke karantina beserta alasannya, sehingga jejaknya tetap ada dan bisa dikembalikan ke pemilik data untuk dikoreksi.

## Aturan Validasi

| Kolom | Aturan |
|---|---|
| `customer_id` | Wajib diisi dan tidak boleh kembar |
| `age` | Angka 18 sampai 100 |
| `contract` | `Monthly` atau `Annual` |
| `monthly_charge` | Angka, tidak boleh negatif |
| `churn` | `Yes` atau `No` |

Sebelum diperiksa, data dirapikan dulu (normalisasi): spasi dibuang dan huruf awal dikapitalkan (`monthly` → `Monthly`), sedangkan angka yang tidak terbaca (mis. `abc`) ditandai kosong agar terdeteksi.

## Hasil

Dari **20 baris** data yang diterima:

| Hasil | Jumlah |
|---|---|
| Data valid | **9** |
| Data karantina | **11** |
| Rekonsiliasi | 9 + 11 = 20 (tidak ada data yang hilang) |

Jumlah baris yang gagal per pemeriksaan:

| Pemeriksaan | Gagal |
|---|---|
| Missing required (kosong) | 4 |
| Duplicate ID (kembar) | 2 |
| Invalid age | 2 |
| Invalid contract | 1 |
| Negative charge | 1 |
| Invalid churn | 1 |

## Struktur Repositori

```
customer-data-validation-pandas/
├── README.md
├── data/
│   └── data_pelanggan_latihan.csv      # data mentah (sintetis)
├── notebooks/
│   ├── Script UK1 - Memasukkan Data.ipynb
│   └── Script UK2 - Memvalidasi Data.ipynb
└── output/
    ├── Data Valid.xlsx                 # 9 baris lolos semua pemeriksaan
    ├── Data Karantina.xlsx             # 11 baris bermasalah + alasan
    └── Laporan Kualitas.xlsx           # ringkasan kualitas, rekonsiliasi, daftar temuan
```

## Cara Menjalankan

### Opsi 1 — Google Colab
1. Buka [colab.research.google.com](https://colab.research.google.com), lalu **File → Upload notebook** dan pilih notebook UK 1.
2. Jalankan sel dari atas ke bawah. Saat diminta, pilih `data/data_pelanggan_latihan.csv`.
3. Unduh `01_data_hasil_pemasukan.csv` yang dihasilkan, lalu buka notebook UK 2 dan unggah file tersebut saat diminta.
4. Jalankan sampai selesai. Tiga file Excel akan dihasilkan.

### Opsi 2 — Lokal (Jupyter / VS Code)
```bash
pip install pandas openpyxl jupyter
```
Letakkan CSV di folder yang sama dengan notebook, jalankan notebook UK 1, lalu UK 2.

## Teknologi

- Python 3
- pandas
- openpyxl (ekspor Excel)

## Penulis

**Evelyn Anastasia**
