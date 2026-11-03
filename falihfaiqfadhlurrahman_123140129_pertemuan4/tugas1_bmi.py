def jalankan_kalkulator_bmi():
    """Fungsi utama untuk menerima input, menghitung, dan mencetak kategori BMI."""
    print("=== PROGRAM PENGHITUNG BMI ===")
    
    berat_kg = float(input("Masukkan berat badan (kg): "))
    tinggi_m = float(input("Masukkan tinggi badan (m): "))
    
    bmi = berat_kg / (tinggi_m * tinggi_m)
    
    if bmi < 18.5:
        kategori = "Berat badan kurang"
    elif 18.5 <= bmi < 25:
        kategori = "Berat badan normal"
    elif 25 <= bmi < 30:
        kategori = "Berat badan berlebih"
    else:
        kategori = "Obesitas"
        
    print("\n--- HASIL ---")
    print(f"Nilai BMI : {bmi:.2f}")
    print(f"Kategori  : {kategori}")

if __name__ == "__main__":
    jalankan_kalkulator_bmi()