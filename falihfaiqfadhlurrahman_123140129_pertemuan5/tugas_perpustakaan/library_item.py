from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """Abstract Base Class untuk seluruh item perpustakaan."""

    def __init__(self, item_id: str, judul: str, tahun_terbit: int):
        self.__item_id = item_id          # Private attribute
        self.__judul = judul              # Private attribute
        self.__tahun_terbit = tahun_terbit  # Private attribute
        self._is_dipinjam = False         # Protected attribute

    # --- Property Getter & Setter ---
    @property
    def item_id(self) -> str:
        return self.__item_id

    @property
    def judul(self) -> str:
        return self.__judul

    @property
    def tahun_terbit(self) -> int:
        return self.__tahun_terbit

    @property
    def is_dipinjam(self) -> bool:
        """Property decorator untuk cek status peminjaman."""
        return self._is_dipinjam

    @is_dipinjam.setter
    def is_dipinjam(self, status: bool):
        if not isinstance(status, bool):
            raise TypeError("Status peminjaman harus berupa boolean!")
        self._is_dipinjam = status

    # --- Abstract Methods ---
    @abstractmethod
    def get_detail(self) -> str:
        """Menampilkan detail informasi item."""
        pass

    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> float:
        """Kalkulasi denda keterlambatan pengembalian."""
        pass


class Book(LibraryItem):
    """Subclass Buku yang mewarisi LibraryItem."""

    def __init__(self, item_id: str, judul: str, tahun_terbit: int, penulis: str, jumlah_halaman: int):
        super().__init__(item_id, judul, tahun_terbit)
        self.penulis = penulis
        self.jumlah_halaman = jumlah_halaman

    def get_detail(self) -> str:
        status_str = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return (f"[BUKU] ID: {self.item_id} | Judul: '{self.judul}' | Penulis: {self.penulis} | "
                f"Tahun: {self.tahun_terbit} | Hal: {self.jumlah_halaman} | Status: {status_str}")

    def hitung_denda(self, hari_terlambat: int) -> float:
        # Tarif denda buku: Rp 2.000 / hari
        return max(0.0, hari_terlambat * 2000.0)


class Magazine(LibraryItem):
    """Subclass Majalah yang mewarisi LibraryItem."""

    def __init__(self, item_id: str, judul: str, tahun_terbit: int, edisi: int, kategori: str):
        super().__init__(item_id, judul, tahun_terbit)
        self.edisi = edisi
        self.kategori = kategori

    def get_detail(self) -> str:
        status_str = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return (f"[MAJALAH] ID: {self.item_id} | Judul: '{self.judul}' | Edisi: #{self.edisi} | "
                f"Kategori: {self.kategori} | Tahun: {self.tahun_terbit} | Status: {status_str}")

    def hitung_denda(self, hari_terlambat: int) -> float:
        # Tarif denda majalah: Rp 3.500 / hari
        return max(0.0, hari_terlambat * 3500.0)