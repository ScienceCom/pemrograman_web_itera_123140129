from library_item import LibraryItem


class Library:
    """Class Pengelola Koleksi Perpustakaan."""

    def __init__(self, nama_perpustakaan: str):
        self.__nama = nama_perpustakaan
        self.__koleksi: list[LibraryItem] = []  # Encapsulated Private List

    @property
    def nama(self) -> str:
        return self.__nama

    def tambah_item(self, item: LibraryItem):
        if not isinstance(item, LibraryItem):
            raise TypeError("Item harus merupakan instance dari LibraryItem!")
        self.__koleksi.append(item)
        print(f"✅ Berhasil menambahkan '{item.judul}' ke {self.__nama}.")

    def tampilkan_katalog(self):
        print(f"\n================ KATALOG PERPUSTAKAAN ({self.__nama}) ================")
        if not self.__koleksi:
            print("Koleksi perpustakaan masih kosong.")
            return

        for idx, item in enumerate(self.__koleksi, 1):
            # Memanggil method polimorfik get_detail()
            print(f"{idx}. {item.get_detail()}")
        print("====================================================================")

    def cari_item(self, keyword: str) -> list[LibraryItem]:
        keyword_lower = keyword.lower()
        hasil = [
            item for item in self.__koleksi
            if keyword_lower in item.judul.lower() or keyword_lower == item.item_id.lower()
        ]
        return hasil

    def pinjam_item(self, item_id: str) -> bool:
        items = self.cari_item(item_id)
        if not items:
            print(f"❌ Item dengan ID '{item_id}' tidak ditemukan.")
            return False

        item = items[0]
        if item.is_dipinjam:
            print(f"⚠️ Item '{item.judul}' sedang dipinjam oleh anggota lain.")
            return False

        item.is_dipinjam = True
        print(f"📖 Berhasil meminjam '{item.judul}'. Selamat membaca!")
        return True

    def kembalikan_item(self, item_id: str, hari_terlambat: int = 0) -> bool:
        items = self.cari_item(item_id)
        if not items:
            print(f"❌ Item dengan ID '{item_id}' tidak ditemukan.")
            return False

        item = items[0]
        if not item.is_dipinjam:
            print(f"⚠️ Item '{item.judul}' tidak dalam status dipinjam.")
            return False

        item.is_dipinjam = False
        denda = item.hitung_denda(hari_terlambat)
        print(f"🔄 Berhasil mengembalikan '{item.judul}'.")
        if denda > 0:
            print(f"💸 Terlambat {hari_terlambat} hari. Denda yang harus dibayar: Rp {denda:,.2f}")
        else:
            print("✨ Pengembalian tepat waktu. Bebas denda.")
        return True