print("[]===== Kalkulator Pintar =====[]")

def add(x, y):
    return x + y
def substract(x, y):
    return x - y
def multiple(x, y):
    return x * y
def divide(x, y):
    return x / y

try:
    a = int(input("Masukkan angka pertama : "))
    b = int(input("Masukkan angka kedua : "))

    print("Pilh Operasi bilangan\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian")
    pilih = int(input("Masukkan operasi : "))

    if pilih == 1:
        print(f"Hasil penjumlahan {a} + {b} = {add(a, b)}")
    elif pilih == 2:
        print(f"Hasil pengurangan {a} - {b} = {substract(a, b)}")
    elif pilih == 3:
        print(f"Hasil perkalian {a} * {b} = {multiple(a, b)}")
    elif pilih == 4:
        print(f"Hasil pembagian {a} / {b} = {divide(a, b)}")
except ValueError:
    print("Program ini hanya menerima jenis nilai integer!")
    exit()
except ZeroDivisionError:
    print("Tidak dapat melakukan pembagian dengan bilangan 0!")
    exit()
except TypeError:
    print("Program ini hanya menerima jenis nilai integer!")
    exit()
except NameError:
    print("Variabel atau fungsi yang dipanggil tidak terdefinisi!")
    exit()
finally:
    print("Terima kasih telah menggunakan kalkulator pintar")