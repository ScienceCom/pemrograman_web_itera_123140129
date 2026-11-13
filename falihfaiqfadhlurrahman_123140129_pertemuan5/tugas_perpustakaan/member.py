class Member:
    """Class untuk mengelola data anggota perpustakaan."""

    def __init__(self, member_id: str, nama: str):
        # Menerapkan Encapsulation dengan Private Attributes
        self.__member_id = member_id
        self.__nama = nama
        self.__pinjaman = []  # List untuk menyimpan ID item yang sedang dipinjam

    # Property Getter untuk mengakses data private secara aman
    @property
    def member_id(self) -> str:
        return self.__member_id

    @property
    def nama(self) -> str:
        return self.__nama

    @property
    def daftar_pinjaman(self) -> list:
        return self.__pinjaman

    # Method Bisnis
    def catat_pinjaman(self, item_id: str):
        """Mencatat ID item yang dipinjam ke dalam daftar pinjaman anggota."""
        self.__pinjaman.append(item_id)

    def hapus_pinjaman(self, item_id: str):
        """Menghapus ID item dari daftar pinjaman setelah dikembalikan."""
        if item_id in self.__pinjaman:
            self.__pinjaman.remove(item_id)

    def get_info_member(self) -> str:
        """Mengembalikan informasi ringkas tentang anggota."""
        jumlah = len(self.__pinjaman)
        return f"Member [{self.__member_id}] {self.__nama} | Meminjam: {jumlah} item"