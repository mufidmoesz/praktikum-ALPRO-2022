angka = int(input('Masukkan angka : '))
print(f'Masukkan angka : {angka}')

if angka > 0:
    print(f'Angka {angka} merupakan bilangan positif')
elif angka < 0:
    print(f'Angka {angka} merupakan bilangan negatif')
elif angka == 0:
    print(f'Angka {angka} merupakan bilangan netral')
else:
    print('Masukkan bilangan yang benar')