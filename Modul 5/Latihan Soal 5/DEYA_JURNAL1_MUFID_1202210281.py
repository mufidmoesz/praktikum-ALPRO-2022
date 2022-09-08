print("------ Nilai Tertinggi? ------")

grades = []
while True:
    grade = input("Masukkan nilai yang kamu dapatkan (ketik 'stop' untuk berhenti) : ")
    if grade == 'stop':
        print(f"Nilai tertinggi yang Suneo dapatkan pada UTS kali ini : {max(grades)}")
        break
    else:
        grades.append(int(grade))