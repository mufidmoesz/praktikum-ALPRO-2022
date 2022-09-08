socmedDaspro = {'nama': 'Daspro Lab', 'password': 'D45P120'}

print(f"Sosmed DASPRO : {socmedDaspro}")

print("===== Menu =====")
print("1. Ganti Nama\n2. Ganti Password\n3. Tampilkan Hasil\n0. Exit")

while True:
    option = int(input("Pilih opsi : "))
    if option == 0:
        print("Terimakasih telah menggunakan program kami")
        break
    elif option == 1:
        nama = input("Masukkan nama baru : ")
        socmedDaspro['nama'] = nama
    elif option == 2:
        password = input("Masukkan password baru : ")
        socmedDaspro['password'] = password
    elif option == 3:
        print("Sosmed DASPRO : ", socmedDaspro)