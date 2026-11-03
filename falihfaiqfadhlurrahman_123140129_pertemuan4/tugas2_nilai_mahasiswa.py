def hitung_grade(nilai_akhir: float) -> str:
    """Mengembalikan grade huruf berdasarkan rentang nilai akhir."""
    if nilai_akhir >= 80:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    else:
        return 'E'

# List 5 dictionary mahasiswa
data_mahasiswa = [
    {"nama": "Falih", "nim": "123140001", "nilai_uts": 80, "nilai_uas": 85, "nilai_tugas": 75},
    {"nama": "Faiq", "nim": "123140002", "nilai_uts": 65, "nilai_uas": 70, "nilai_tugas": 80},
    {"nama": "Fadhlu", "nim": "123140003", "nilai_uts": 90, "nilai_uas": 92, "nilai_tugas": 88},
    {"nama": "Rahman", "nim": "123140004", "nilai_uts": 50, "nilai_uas": 45, "nilai_tugas": 60},
    {"nama": "Fufufafa", "nim": "123140005", "nilai_uts": 75, "nilai_uas": 78, "nilai_tugas": 70}
]

print("=== REKAP NILAI MAHASISWA ===")
print(f"{'Nama':<10} | {'NIM':<10} | {'Nilai Akhir':<11} | {'Grade'}")
print("-" * 45)

list_nilai_akhir = []

for mhs in data_mahasiswa:
    # Perhitungan persentase bobot
    nilai_akhir = (0.30 * mhs["nilai_uts"]) + (0.40 * mhs["nilai_uas"]) + (0.30 * mhs["nilai_tugas"])
    grade = hitung_grade(nilai_akhir)

    # Menyimpan nilai akhir untuk pencarian min/max
    mhs["nilai_akhir"] = nilai_akhir 
    list_nilai_akhir.append(nilai_akhir)
    
    print(f"{mhs['nama']:<10} | {mhs['nim']:<10} | {nilai_akhir:<11.2f} | {grade}")

# Mendeteksi nilai tertinggi dan terendah
nilai_tertinggi = max(list_nilai_akhir)
nilai_terendah = min(list_nilai_akhir)

print("-" * 45)
print(f"Nilai Akhir Tertinggi : {nilai_tertinggi:.2f}")
print(f"Nilai Akhir Terendah  : {nilai_terendah:.2f}")