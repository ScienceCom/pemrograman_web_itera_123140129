PI = 3.14159

# 1. Fungsi Luas & Keliling: Persegi
def luas_persegi(sisi: float) -> float:
    """Menghitung luas persegi."""
    return sisi * sisi

def keliling_persegi(sisi: float) -> float:
    """Menghitung keliling persegi."""
    return 4 * sisi

# 2. Fungsi Luas & Keliling: Persegi Panjang
def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang."""
    return panjang * lebar

def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung keliling persegi panjang."""
    return 2 * (panjang + lebar)

# 3. Fungsi Luas & Keliling: Lingkaran
def luas_lingkaran(jari_jari: float) -> float:
    """Menghitung luas lingkaran menggunakan konstanta PI."""
    return PI * (jari_jari ** 2)

def keliling_lingkaran(jari_jari: float) -> float:
    """Menghitung keliling lingkaran menggunakan konstanta PI."""
    return 2 * PI * jari_jari

# 4. Fungsi Konversi Suhu
def celsius_ke_fahrenheit(celsius: float) -> float:
    """Mengonversi suhu dari Celsius ke Fahrenheit."""
    return (celsius * 9/5) + 32

def celsius_ke_kelvin(celsius: float) -> float:
    """Mengonversi suhu dari Celsius ke Kelvin."""
    return celsius + 273.15