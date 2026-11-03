## Identitas

**Nama:** Falih Faiq Fadhlurrahman

**NIM:** 123140129

**Mata Kuliah:** Praktikum Pengembangan Aplikasi Web

---

## 1. Deskripsi Alur Kerja dan Fungsi Program

### Tugas 1: Program Penghitung BMI (`tugas1_bmi.py`)
Program ini meminta input berupa berat badan (kg) dan tinggi badan (m) dari pengguna melalui terminal. Alur kerjanya menghitung nilai *Body Mass Index* (BMI) dengan rumus `berat / (tinggi * tinggi)`. Setelah mendapatkan nilai numeriknya, program mengevaluasi nilai tersebut menggunakan struktur kendali `if-elif-else` untuk mengklasifikasikan pengguna ke dalam salah satu dari empat kategori: "Berat badan kurang", "Berat badan normal", "Berat badan berlebih", atau "Obesitas".

### Tugas 2: Pengelolaan Data Nilai Mahasiswa (`tugas2_nilai_mahasiswa.py`)
Program ini mengelola koleksi data mahasiswa dalam bentuk *list of dictionaries*. Alur kerjanya melakukan iterasi (`for` loop) pada setiap mahasiswa untuk menghitung Nilai Akhir dengan pembobotan 30% UTS, 40% UAS, dan 30% Tugas. Nilai akhir tersebut kemudian dievaluasi menggunakan fungsi `hitung_grade()` untuk menentukan nilai huruf (A-E). Program juga menyimpan setiap nilai akhir ke dalam sebuah *list* terpisah untuk mencari nilai tertinggi (`max()`) dan terendah (`min()`), lalu menampilkan seluruh rekapitulasi dalam format tabel yang rapi.

### Tugas 3: Modul Matematika (`math_operations.py` dan `main.py`)
Tugas ini menerapkan modularitas fungsi. 
*   **`math_operations.py`:** Bertindak sebagai modul kustom yang menyimpan definisi konstanta `PI`, fungsi-fungsi perhitungan luas dan keliling geometri (persegi, persegi panjang, lingkaran), serta fungsi konversi suhu (Celsius ke Fahrenheit dan Kelvin)[cite: 28, 29].
*   **`main.py`:** Bertindak sebagai skrip utama. Program ini mendemonstrasikan dua cara impor: mengimpor keseluruhan modul dengan alias (`import math_operations as math_ops`) dan mengimpor fungsi spesifik ke namespace lokal (`from math_operations import ...`). Program kemudian memanggil seluruh fungsi dengan argumen uji dan mencetak hasilnya.

---

## 2. Instruksi Cara Menjalankan Skrip di Terminal

Pastikan terminal sudah berada di dalam direktori folder praktikum ini.

1.  Menjalankan Tugas 1 (Kalkulator BMI):
    Ketikan perintah berikut di terminal:
``bash
python tugas1_bmi.py

2.  Menjalankan Tugas 2 (Data Nilai Mahasiswa):
    Ketikan perintah berikut di terminal:
``bash
python tugas1_bmi.pypython tugas2_nilai_mahasiswa.py

3.  Menjalankan Tugas 3 (Modul Matematika):
    Ketikan perintah berikut di terminal:
``bash
python main.py

---

## 3. Screenshot
