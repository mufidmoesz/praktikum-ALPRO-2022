def luas(x, y):
    return x * y

def keliling(x, y):
    return 2 * (x + y)

length = float(input("Masukkan panjang: "))
width = float(input("Masukkan lebar: "))

print(f"Luas Tanah adalah: {luas(length, width)} m^2")
print(f"Keliling Tanah adalah: {keliling(length, width)} m")