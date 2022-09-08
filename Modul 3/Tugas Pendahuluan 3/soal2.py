print('===Mini Market Daspro===')
print('1. Sayur\n2. Buah\n3. Daging\n0. Cek Keranjang')

sayur = 0
buah = 0
daging = 0
loop = True
while loop:
    beli = int(input('Mau beli menu nomor berapa?: '))
    if beli == 0:
        loop = False
    else:
        item = int(input('Berapa banyak?: '))
        if beli == 1:
            sayur = sayur + item
            print(item, 'Sayur telah ditambahkan ke dalam keranjang')
        elif beli == 2:
            buah = buah + item
            print(item, 'Buah telah ditambahkan ke dalam keranjang')
        elif beli == 3:
            daging = daging + item
            print(item, 'Daging telah ditambahkan ke dalam keranjang')
        elif beli == 0:
            loop = False
        else:
            print('Menu tidak tersedia')

print('Isi Keranjangmu :')
print(f'- {sayur} Sayur\n- {buah} Buah\n- {daging} Daging')