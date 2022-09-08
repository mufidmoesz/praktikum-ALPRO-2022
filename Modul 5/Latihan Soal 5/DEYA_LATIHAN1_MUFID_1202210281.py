print("===>>> PROGRAM WISHLIST ANIME <<<===")
print("1. Tambah Anime Ke Wishlist")
print("2. Mengurutkan Daftar Anime")
print("3. Menampilkan Seluruh Judul Anime")
print("0. Exit")

wishlist = []

while True:
    menu = int(input("Masukkan menu yang anda inginkan : "))
    if menu == 0:
        print("Terimakasih telah menggunakan program kami")
        break
    elif menu == 1:
        anime = input("Masukkan judul anime : ")
        wishlist.append(anime)
        print(f"{anime} berhasil ditambahkan")
    elif menu == 2:
        wishlist.sort()
        print("Wishlist anime telah diurutkan")
    elif menu == 3:
        for i in range(len(wishlist)):
            print(f"{i+1}. {wishlist[i]}")
    else:
        print("Menu yang anda masukkan tidak tersedia, silahkan pilih menu lain")