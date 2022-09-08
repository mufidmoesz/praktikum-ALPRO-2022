print('===== Toko Laptop Davidcomp =====')

laptop = input('Masukkan merk laptop : ')
print('Masukkan Merk Laptop :', laptop)

match laptop.lower():
    case 'asus':
        print('\t==Katalog Laptop Asus==')
        print('\tModel : Asus Vivobook')
        print('\tHarga : 5.500.000\n')
        print('\tModel : Asus TUF')
        print('\tHarga : 12.000.000')
    case 'lenovo':
        print('\t==Katalog Laptop Lenovo==')
        print('\tModel : Lenovo Thinkpad')
        print('\tHarga : 7.500.000\n')
        print('\tModel : Lenovo Ideapad')
        print('\tHarga : 10.000.000')
    case 'acer':
        print('\t==Katalog Laptop Acer==')
        print('\tModel : Acer Aspire')
        print('\tHarga : 4.500.000\n')
        print('\tModel : Acer Swift')
        print('\tHarga : 13.000.000')
    case _:
        print('\tLaptop merk', laptop, 'tidak ada')