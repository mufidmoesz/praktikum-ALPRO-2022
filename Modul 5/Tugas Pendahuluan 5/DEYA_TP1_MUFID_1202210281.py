print("===>>> PROGRAM MANAJEMEN DATA PENDAPATAN PENJUALAN CILOK <<<===")
print("1. Tambah Data Pendapatan")
print("2. Mengurutkan Data (dari yang terbesar)")
print("3. Menghitung Total Pendapatan")
print("4. Menghapus Data Pendapatan")
print("5. Menampilkan Seluruh Data Pendapatan")
print("0. Keluar")

data = []
while True:
    menu = int(input("Masukkan menu yang anda inginkan: "))
    if menu == 0:
        print("Terima kasih telah menggunakan program kami")
        break
    elif menu == 1:
        penjualan = int(input("Masukkan data pendapatan penjualan cilok: "))
        data.append(penjualan)
        print(f"Data pendapatan penjualan cilok sebesar {penjualan} berhasil ditambahkan")
    elif menu == 2:
        data.sort(reverse=True)
        print("Data penjualan cilok telah diurutkan")
    elif menu == 3:
        print(f"Total pendapatan penjualan cilok adalah {sum(data)}")
    elif menu == 4:
        delete = int(input("Masukkan data pendapatan penjualan cilok yang ingin dihapus: "))
        if delete in data:
            data.remove(delete)
            print(f"Data pendapatan penjualan cilok sebesar {delete} berhasil dihapus")
        else:
            print("Data tidak ditemukan")
    elif menu == 5:
        print("Data penjualan cilok: ")
        for i in data:
            x = 1
            print(f"{x}. {i}")
            x += 1
    else:
        print("Menu yang anda pilih tidak tersedia, silahkan pilih menu lain")
