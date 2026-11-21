# RESTful API Manajemen Mahasiswa & Matakuliah

Backend RESTful API berbasis **Pyramid Framework**, **SQLAlchemy ORM**, **Alembic**, dan **PostgreSQL** untuk mengelola data Mahasiswa dan Matakuliah.

* **Nama:** Falih Faiq Fadhlurrahman
* **NIM:** 123140129
* **Kelas:** Pengembangan Aplikasi Web RB

---

## Teknologi
* Python 3.11+, Pyramid, Waitress
* SQLAlchemy, Alembic, `pyramid_tm`
* PostgreSQL

---

## Instalasi & Menjalankan Aplikasi

1. **Aktifkan Virtual Environment & Instal Dependensi**
   ```powershell
   .\venv\bin\Activate.ps1
   cd pyramid_mahasiswa
   pip install -e ".[testing]"
   pip install psycopg pyramid_tm zope.sqlalchemy
   ```

2. **Setup Database PostgreSQL**
   Buat database `pyramid_mahasiswa` dan user `pyramid_user` (password `666`), lalu sesuaikan `development.ini`:
   ```ini
   sqlalchemy.url = postgresql+psycopg://pyramid_user:666@localhost:5432/pyramid_mahasiswa
   ```

3. **Migrasi Database & Seeding Data**
   ```powershell
   alembic -c development.ini revision --autogenerate -m "create mahasiswa and matakuliah tables"
   alembic -c development.ini upgrade head
   python -m pyramid_mahasiswa.scripts.initialize_db development.ini
   ```

4. **Jalankan Server**
   ```powershell
   pserve development.ini --reload
   ```
   Akses API di `http://localhost:6543`.

---

## Daftar Endpoint API

| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| `GET` | `/` | Cek status API |
| `GET` | `/api/mahasiswa` | Ambil semua data mahasiswa |
| `GET` | `/api/mahasiswa/{id}` | Ambil detail mahasiswa |
| `POST` | `/api/mahasiswa` | Tambah mahasiswa baru |
| `PUT` | `/api/mahasiswa/{id}` | Update data mahasiswa |
| `DELETE` | `/api/mahasiswa/{id}` | Hapus data mahasiswa |
| `GET` | `/api/matakuliah` | Ambil semua data matakuliah |
| `GET` | `/api/matakuliah/{id}` | Ambil detail matakuliah |
| `POST` | `/api/matakuliah` | Tambah matakuliah baru (`sks` & `semester` > 0) |
| `PUT` | `/api/matakuliah/{id}` | Update data matakuliah |
| `DELETE` | `/api/matakuliah/{id}` | Hapus data matakuliah |

---

## Pengujian (`curl.exe`)

```powershell
# Mahasiswa
curl.exe -X GET http://localhost:6543/api/mahasiswa
curl.exe -X GET http://localhost:6543/api/mahasiswa/1
curl.exe --% -X POST http://localhost:6543/api/mahasiswa -H "Content-Type: application/json" -d "{\"nim\": \"67890\", \"nama\": \"Ahmad Fadli\", \"jurusan\": \"Teknik Elektro\", \"tanggal_lahir\": \"2001-11-05\", \"alamat\": \"Jl. Mawar No. 10, Surabaya\"}"
curl.exe --% -X PUT http://localhost:6543/api/mahasiswa/1 -H "Content-Type: application/json" -d "{\"jurusan\": \"Informatika Medis\", \"alamat\": \"Jl. Dipati Ukur No. 88, Bandung\"}"
curl.exe -X DELETE http://localhost:6543/api/mahasiswa/3

# Matakuliah
curl.exe -X GET http://localhost:6543/api/matakuliah
curl.exe -X GET http://localhost:6543/api/matakuliah/1
curl.exe --% -X POST http://localhost:6543/api/matakuliah -H "Content-Type: application/json" -d "{\"kode_mk\": \"IF4110\", \"nama_mk\": \"Kecerdasan Buatan\", \"sks\": 3, \"semester\": 7}"
curl.exe --% -X PUT http://localhost:6543/api/matakuliah/1 -H "Content-Type: application/json" -d "{\"nama_mk\": \"Algoritma dan Struktur Data Lanjut\", \"sks\": 4}"
curl.exe -X DELETE http://localhost:6543/api/matakuliah/4
```

---

## Dokumentasi Pengujian

* **CRUD Mahasiswa**
  <img src="crud_mahasiswa.png" width="800" />
* **CRUD Matakuliah**
  <img src="crud_matakuliah.png" width="800" />
