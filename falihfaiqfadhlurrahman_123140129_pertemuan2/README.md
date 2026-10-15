# Dashboard Studi Teknik Informatika

**Identitas:**
- **Nama Lengkap:** Falih Faiq Fadhlurrahman
- **NIM:** 123140129
- **Kelas Praktikum:** Pengembangan Aplikasi Web RB

---

Aplikasi ini tidak hanya berfungsi sebagai *To-Do List* atau pencatat agenda, tetapi juga dilengkapi dengan fitur pemantau **Cuaca Real-time** terintegrasi. Fitur cuaca ini sangat berguna bagi mahasiswa untuk memantau kondisi cuaca di area kampus (suhu dan kecepatan angin) sebelum memutuskan untuk berangkat kuliah atau praktikum.

### Fitur Utama:
1. **Manajemen Agenda (CRUD):** Pengguna dapat menambah, mengedit, menghapus, dan menandai tugas yang sudah selesai.
2. **Kategorisasi Tugas:** Setiap agenda dapat dikategorikan menjadi *Kuliah Umum, Praktikum, Proyek, atau Lainnya*.
3. **Penyimpanan Lokal Persisten:** Seluruh data agenda disimpan di dalam `localStorage` browser sehingga data tidak akan hilang ketika halaman dimuat ulang (refresh) atau browser ditutup.
4. **Cuaca Real-Time:** Menarik data cuaca aktual secara langsung dari *Open-Meteo API* (tanpa API Key) menggunakan operasi *Asynchronous*.

---

## Implementasi Fitur ES6+ Wajib
Sesuai dengan kriteria penilaian praktikum, aplikasi ini telah mengimplementasikan konsep JavaScript Modern (ES6+). Berikut adalah daftar fitur beserta lokasinya pada file `app.js`:

### 1. Classes (OOP - Object Oriented Programming)
- **Baris 2 - 8:** Pembuatan class `TaskItem` sebagai blueprint/model data murni untuk setiap tugas.
- **Baris 11 - 131:** Pembuatan class `DashboardApp` sebagai *controller* utama yang mengelola logika DOM, LocalStorage, dan State Management.

### 2. Deklarasi Variabel Modern (`let` dan `const`)
- **Baris 13:** Penggunaan `const savedData` (karena nilai dari localStorage awal tidak akan di-reassign).
- **Baris 16 - 21:** Penggunaan `const` untuk mendeklarasikan berbagai elemen DOM (`this.form`, `this.titleInput`, dll) untuk menghindari perubahan referensi secara tidak sengaja.

### 3. Arrow Functions (`() => {}`)
Digunakan secara ekstensif pada *method* di dalam Class agar konteks `this` tetap mengikat (binding) pada *instance* class `DashboardApp`.
- **Baris 30:** `bindEvents = () => { ... }`
- **Baris 47:** `fetchWeather = async () => { ... }`
- **Baris 63:** `addTask = (title, category) => { ... }`
- **Baris 109:** `render = () => { ... }`

### 4. Fungsi Asinkron (Async / Await)
- **Baris 47 - 60:** Implementasi `async / await` pada *method* `fetchWeather` untuk melakukan *HTTP Request* (Fetch API) ke server Open-Meteo secara non-blocking. Terdapat juga implementasi blok `try...catch` untuk *Error Handling* jika API gagal dimuat.

### 5. Destructuring Object
- **Baris 53 (Nested Destructuring):** `const { current_weather: { temperature, windspeed } } = data;` -> Mengekstrak langsung nilai suhu dan kecepatan angin dari dalam *nested object* respons API.
- **Baris 116:** `const { id, title, category, completed } = task;` -> Mengekstrak properti dari objek `task` saat proses *mapping* untuk *rendering*.

### 6. Template Literals (`` `...` ``)
- **Baris 57:** `` this.weatherInfo.textContent = `${temperature}°C \vert{} Angin:${windspeed} km/h`; `` -> Digunakan untuk menyisipkan nilai variabel langsung ke dalam teks informasi cuaca.
- **Baris 118 - 128:** Digunakan di dalam perulangan `.map()` untuk memanipulasi dan mencetak struktur HTML (DOM) secara dinamis ke halaman web.

### 7. Spread Operator (`...`) & Immutability (*Nilai Plus*)
- **Baris 68:** `this.tasks = [...this.tasks, newTask];` -> Menyisipkan data baru tanpa memutasi array asli (menggantikan `.push()`).
- **Baris 82 & 90:** `{ ...task, title: newTitle.trim() }` -> Memperbarui *state* objek pada fitur *Edit* dan *Toggle Completed* menggunakan teknik duplikasi dengan spread operator.