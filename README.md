# ETL Pipeline Project – Fashion Product Data

## Ringkasan Proyek

Proyek ini merupakan implementasi **ETL Pipeline (Extract, Transform, Load)** untuk memproses data produk fashion dari sebuah website sumber dan menyimpannya ke media penyimpanan yang siap digunakan untuk analisis lanjutan. Proyek ini dikembangkan sebagai bagian dari submission *Fundamental Pemrosesan Data* dan dirancang sebagai **portfolio teknikal** untuk menunjukkan pemahaman praktis terkait data engineering dasar.

Pipeline ini mencakup proses pengambilan data secara otomatis (web scraping), pembersihan dan transformasi data, serta pemuatan data ke dalam format yang umum digunakan di dunia industri, yaitu **CSV file** dan **Google Sheets**.

---

## Problem Statement

Banyak data yang tersedia di web masih bersifat tidak terstruktur dan tidak siap langsung digunakan untuk analisis. Oleh karena itu dibutuhkan proses ETL untuk:

* Mengambil data mentah dari sumber eksternal
* Membersihkan dan menstandarkan data
* Menyimpan data ke dalam format yang terstruktur dan mudah diakses

Proyek ini menjawab kebutuhan tersebut dengan membangun pipeline ETL sederhana namun lengkap menggunakan Python.

---

## Tujuan Proyek

1. Membangun ETL pipeline modular menggunakan Python.
2. Melakukan web scraping data produk fashion dari website sumber.
3. Melakukan transformasi data agar konsisten dan bersih.
4. Menyimpan hasil akhir ke file CSV dan Google Sheets.
5. Menyediakan unit test dan test coverage untuk memastikan kualitas kode.

---

## Sumber Data

* **Website**: [https://fashion-studio.dicoding.dev](https://fashion-studio.dicoding.dev)
* **Jenis Data**: Produk fashion
* **Metode Extract**: HTTP request dan HTML parsing (web scraping)

---

## Arsitektur ETL Pipeline

Pipeline dibangun mengikuti konsep ETL klasik:

### 1. Extract

Tahap extract bertugas mengambil data mentah dari website sumber.

Teknik yang digunakan:

* HTTP request untuk mengambil halaman web
* Parsing HTML menggunakan BeautifulSoup

Data yang diekstrak meliputi informasi produk seperti:

* Nama produk
* Harga
* Kategori
* Informasi tambahan yang tersedia di halaman produk

---

### 2. Transform

Tahap transform bertujuan membersihkan dan menstandarkan data sebelum disimpan.

Proses transformasi meliputi:

* Menghapus karakter tidak diperlukan
* Konversi tipe data (misalnya harga menjadi numerik)
* Penyesuaian format kolom agar konsisten
* Validasi data kosong atau tidak valid

Hasil dari tahap ini adalah dataset yang sudah bersih dan siap dimuat ke sistem penyimpanan.

---

### 3. Load

Tahap load menyimpan data hasil transformasi ke dua media output:

1. **File CSV**

   * Digunakan sebagai format penyimpanan lokal
   * Mudah digunakan untuk analisis lanjutan

2. **Google Sheets**

   * Menggunakan Google Sheets API
   * Memungkinkan data diakses dan dibagikan secara online
   * Cocok untuk kolaborasi dan monitoring

---

## Struktur Project

Struktur proyek dirancang modular agar mudah dipahami dan dikembangkan.

```
project-root/
│
├── main.py                # Entry point pipeline ETL
├── extract/               # Modul extract (web scraping)
├── transform/             # Modul transform (data cleaning)
├── load/                  # Modul load (CSV & Google Sheets)
├── tests/                 # Unit test untuk setiap modul
├── requirements.txt       # Daftar dependensi
├── google-sheets-api.json # Credential Google Sheets API
└── README.md
```

---

## Testing dan Quality Assurance

Proyek ini dilengkapi dengan pengujian untuk memastikan setiap komponen pipeline bekerja dengan benar.

### Unit Testing

* Framework: `pytest`
* Fokus pada pengujian fungsi extract, transform, dan load

### Test Coverage

* Tool: `coverage`
* Digunakan untuk memastikan sebagian besar kode teruji

Testing ini menunjukkan perhatian terhadap kualitas kode dan praktik pengembangan yang baik.

---

## Teknologi yang Digunakan

* Python
* Requests
* BeautifulSoup4
* Pandas
* GSpread
* OAuth2Client
* Pytest
* Coverage

---

## Nilai Teknis Proyek

Proyek ini menunjukkan kemampuan dalam:

* Membangun ETL pipeline end-to-end
* Web scraping dan data ingestion
* Data cleaning dan transformasi
* Integrasi dengan Google Sheets API
* Penulisan kode modular dan terstruktur
* Penerapan unit testing dan test coverage

---

## Potensi Pengembangan

Beberapa pengembangan lanjutan yang dapat dilakukan:

* Menambahkan logging dan error handling yang lebih detail
* Menjadwalkan pipeline menggunakan cron atau workflow orchestrator
* Menyimpan data ke database (PostgreSQL / MySQL)
* Menambahkan incremental load
* Dockerisasi pipeline untuk deployment

---

## Kesimpulan

Proyek ETL Pipeline ini merepresentasikan implementasi nyata pemrosesan data dari sumber eksternal hingga siap digunakan untuk analisis. Dengan pendekatan modular, testing yang memadai, dan integrasi API eksternal, proyek ini cocok dijadikan portfolio untuk posisi magang di bidang data engineering, data analyst, maupun software engineering dengan fokus data.

---
