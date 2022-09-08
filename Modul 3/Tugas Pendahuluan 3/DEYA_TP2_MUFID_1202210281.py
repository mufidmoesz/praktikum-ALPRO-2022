print('===Mini Market Daspro===')
print('1. Sayur\n2. Buah\n3. Daging\n0. Cek Keranjang')

sayur = 0
buah = 0
daging = 0
loop = True
while loop:
    beli = int(input('Mau beli menu nomor berapa?: '))
    match beli:
        case 1:
            item = int(input('Berapa banyak?: '))
            sayur = sayur + item
            print(item, 'Sayur telah ditambahkan ke dalam keranjang')
        case 2:
            item = int(input('Berapa banyak?: '))
            buah = buah + item
            print(item, 'Buah telah ditambahkan ke dalam keranjang')
        case 3:
            item = int(input('Berapa banyak?: '))
            daging = daging + item
            print(item, 'Daging telah ditambahkan ke dalam keranjang')
        case 0:
            loop = False
        case _:
            print('Menu tidak tersedia')
        
print('\nIsi Keranjangmu :')
print(f'- {sayur} Sayur\n- {buah} Buah\n- {daging} Daging')