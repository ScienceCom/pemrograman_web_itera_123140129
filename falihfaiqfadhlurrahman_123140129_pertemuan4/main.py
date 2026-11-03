import math_operations as math_ops
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin

print("=== PENGUJIAN MODUL MATEMATIKA ===")

print("\n--- 1. BANGUN DATAR ---")
sisi = 5
print(f"Persegi (sisi {sisi}):")
print(f" - Luas     : {math_ops.luas_persegi(sisi)}")
print(f" - Keliling : {math_ops.keliling_persegi(sisi)}")

panjang, lebar = 10, 4
print(f"\nPersegi Panjang (panjang {panjang}, lebar {lebar}):")
print(f" - Luas     : {math_ops.luas_persegi_panjang(panjang, lebar)}")
print(f" - Keliling : {math_ops.keliling_persegi_panjang(panjang, lebar)}")

jari2 = 7
print(f"\nLingkaran (jari-jari {jari2}):")
print(f" - Luas     : {math_ops.luas_lingkaran(jari2):.2f}")
print(f" - Keliling : {math_ops.keliling_lingkaran(jari2):.2f}")

print("\n--- 2. KONVERSI SUHU ---")
suhu_c = 30
suhu_f = celsius_ke_fahrenheit(suhu_c)
suhu_k = celsius_ke_kelvin(suhu_c)

print(f"Suhu Awal : {suhu_c}°C")
print(f"Fahrenheit: {suhu_f}°F")
print(f"Kelvin    : {suhu_k} K")