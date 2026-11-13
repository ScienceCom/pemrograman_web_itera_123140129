from library import Library
from library_item import Book, Magazine
from member import Member

if __name__ == "__main__":
    print("=== SISTEM MANAJEMEN PERPUSTAKAAN ===")

    # 1. Instansiasi Perpustakaan
    perpus = Library("Perpustakaan Utama ITERA")

    # 2. Tambah Item (Buku & Majalah)
    buku1 = Book("BK001", "Pemrograman Web dengan Python", 2024, "Ahmad Fadhil", 350)
    buku2 = Book("BK002", "Struktur Data & Algoritma", 2023, "Siti Rahma", 420)
    majalah1 = Magazine("MJ001", "Tech Monthly - AI Edition", 2026, 45, "Teknologi")

    print("\n--- 1. Menambahkan Item ---")
    perpus.tambah_item(buku1)
    perpus.tambah_item(buku2)
    perpus.tambah_item(majalah1)

    # 3. Tampilkan Katalog
    perpus.tampilkan_katalog()

    # 4. Cari Item
    print("\n--- 2. Uji Coba Pencarian ---")
    pencarian = perpus.cari_item("Python")
    print(f"Hasil pencarian kata kunci 'Python' ({len(pencarian)} ditemukan):")
    for item in pencarian:
        print(f" -> {item.get_detail()}")

    # 5. Transaksi Peminjaman
    print("\n--- 3. Uji Coba Peminjaman Item ---")
    perpus.pinjam_item("BK001")
    perpus.pinjam_item("BK001")  # Coba pinjam item yang sama lagi

    # Tampilkan katalog setelah dipinjam
    perpus.tampilkan_katalog()

    # 6. Transaksi Pengembalian & Kalkulasi Denda (Polimorfisme hitung_denda)
    print("\n--- 4. Uji Coba Pengembalian & Denda ---")
    # Pengembalian terlambat 3 hari untuk buku
    perpus.kembalikan_item("BK001", hari_terlambat=3)

    # Pinjam dan kembalikan majalah terlambat 2 hari
    perpus.pinjam_item("MJ001")
    perpus.kembalikan_item("MJ001", hari_terlambat=2)

    print("\n--- 5. Uji Coba Member ---")
    member1 = Member("M001", "Budi Santoso")
    print(member1.get_info_member())

    # Simulasi pencatatan pinjaman ke anggota
    member1.catat_pinjaman("BK001")
    print(f"{member1.nama} meminjam buku. " + member1.get_info_member())

    # Status akhir
    perpus.tampilkan_katalog()