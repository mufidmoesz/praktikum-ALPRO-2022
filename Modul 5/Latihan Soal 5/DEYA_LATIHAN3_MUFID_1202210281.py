setA = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
setB = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

print("\t>> HIMPUNAN <<")
print("1. Menggabungkan 2 set (union)\n2. Irisan 2 set (intersection)\n3. Selisih 2 set (difference)\n4. New set (update)\n0. Exit")
print(f"Set A berisikan angka : {setA}")
print(f"Set B berisikan angka : {setB}")


setD = {16, 17, 18, 19, 20}
while True:
    menu = int(input("Pilih menu : "))
    if menu == 0:
        print("Terimakasih telah menggunakan program kami")
        break
    elif menu == 1:
        print(setA.union(setB))
    elif menu == 2:
        print(setA.intersection(setB))
    elif menu == 3:
        print(setA.difference(setB))
    elif menu == 4:
        setA.update(setB.union(setD))
        print(f"Set A telah diupdate menjadi : {setA}")
    else:
        print("Kamu hanya boleh pilih menu sampai 4!")