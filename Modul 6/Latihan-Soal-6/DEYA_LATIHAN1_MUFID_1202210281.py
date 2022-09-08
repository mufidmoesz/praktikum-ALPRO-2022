import numpy as np  

print("PROGRAM MENGHITUNG RATA-RATA")

grades = []
try:
    banyakNilai = int(input("Ingin menghitung berapa nilai : "))
    for i in range(banyakNilai):
        grade = int(input(f"Masukkan nilai ke-{i+1} : "))
        grades.append(grade)

    print(f"Hasil rata rata yang didapat adalah {np.mean(grades)}")
except ValueError:
    print("Program ini hanya menerima jenis nilai integer!")
    exit()
finally:
    print("Program Selesai")
