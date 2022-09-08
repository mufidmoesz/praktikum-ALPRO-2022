kata = input("Masukkan kata : ")
tuple1 = tuple(kata)

print("==== Menu Tuple ====")
print("1. Tampilkan kata dalam bentuk tuple\n2. Jumlah Huruf\n3. Membalik Urutan\n0. Exit")

while True:
    opsi = int(input("pilih opsi : "))
    if opsi == 0:
        print("Terimakasih telah menggunakan program kami")
        break
    elif opsi == 1:
        print(f"Kata dalam bentuk tuple : {tuple1}")
    elif opsi == 2:
        print(f"Jumlah huruf : {len(tuple1)}")
    elif opsi == 3:
        print(f"Hasil membalikkan urutan : {tuple1[::-1]}")
    else:
        print("Menu tidak ada, silahkan pilih menu lain")
        