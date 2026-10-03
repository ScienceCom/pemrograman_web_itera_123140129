# Mini POS - Aplikasi Kasir & Keranjang Belanja Sederhana

**Identitas:**
- **Nama Lengkap:** Falih Faiq Fadhlurrahman
- **NIM:** 123140129
- **Kelas Praktikum:** Pemrograman Aplikasi Web RB

---

## Deskripsi Aplikasi
Aplikasi Mini POS ini adalah sistem kasir berbasis web sederhana yang dirancang untuk toko kampus atau kantin. Aplikasi ini memungkinkan kasir untuk menginput barang, menghitung total harga (subtotal dan total akhir), memberikan diskon otomatis, serta menghitung uang kembalian. Seluruh data belanja disimpan dalam browser menggunakan LocalStorage agar tidak hilang saat halaman dimuat ulang (refresh).

## Panduan Menjalankan
1. Pastikan Anda sudah menginstal Text Editor seperti **Visual Studio Code (VS Code)**.
2. Unduh atau clone repository ini ke komputer lokal Anda.
3. Buka folder proyek di VS Code.
4. Instal ekstensi **Live Server** di VS Code.
5. Buka file `index.html`.
6. Klik kanan pada jendela kode dan pilih **"Open with Live Server"**. Browser akan otomatis terbuka dan menjalankan aplikasi.

## Daftar Fitur
- [x] **Validasi Form Input**: Memastikan nama (min 3 huruf), harga (min Rp 500), dan qty (min 1) diisi dengan benar. Mencegah input kosong/negatif.
- [x] **Kalkulator & Perhitungan**: Otomatis menghitung subtotal barang, total keseluruhan, dan diskon 10% jika transaksi mencapai minimal Rp 50.000.
- [x] **Kalkulator Uang Kembalian**: Menghitung uang kembalian pelanggan serta memberikan peringatan jika uang yang dibayarkan kurang.
- [x] **Manajemen Keranjang (Hapus & Reset)**: Pengguna dapat menghapus item spesifik atau mereset transaksi sepenuhnya.
- [x] **Penyimpanan Persisten (LocalStorage)**: Memanfaatkan `localStorage` JSON untuk mempertahankan data di browser.
- [x] **Implementasi Fetch API**: Menggunakan asinkronus `fetch` untuk memuat informasi toko/pengumuman secara dinamis saat halaman pertama kali dimuat.

## Penjelasan Teknis Singkat
1. **Validasi Input:** Dilakukan di fungsi event handler `submit`. Menggunakan `if-else` untuk mengecek validitas input dan menampilkan error di `<small>` tag sebelum data di-push ke array `cart`.
2. **Algoritma Kalkulator:** Memanfaatkan metode Array `reduce()` untuk mengakumulasi nilai `subtotal` menjadi `totalBelanja`. Logika diskon hanya aktif jika `totalBelanja >= 50000`.
3. **Mekanisme Serialisasi LocalStorage:** Tiap kali ada perubahan (tambah/hapus barang), fungsi `simpanKeLocalStorage()` dipanggil untuk mengubah array object menjadi string menggunakan `JSON.stringify(cart)` dan saat dimuat kembali menggunakan `JSON.parse()`.

## Tangkapan Layar (Screenshot)
*(Silakan buat folder `assets/` dan letakkan screenshot aplikasi Anda, lalu ubah link di bawah ini)*
- **Tampilan Form Utama:** `![Form Utama](assets/screenshot-1.png)`
- **Tampilan Error Validasi:** `![Error Validasi](assets/screenshot-2.png)`
- **Tampilan Hasil Kalkulator:** `![Kalkulator](assets/screenshot-3.png)`