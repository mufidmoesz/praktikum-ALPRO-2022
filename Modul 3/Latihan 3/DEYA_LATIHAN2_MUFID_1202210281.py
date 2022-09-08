print('Daftar barang yang tersedia di toko fashion melromarc')
print('1. Kemeja => Rp.50000\n2. Celana => Rp.60000\n3. Sepatu => Rp.30000')

kemeja = 50000
celana = 60000
sepatu = 30000

price = 0
amount = int(input('Berapa barang yang ingin dibeli : '))
for i in range(amount):
    item = input('Masukkan kode barang yang ingin dibeli (1/2/3/selesai) : ')
    if item == '1':
        price += kemeja
        print('Kemeja Ditambahkan')
    if item == '2':
        price += celana
        print('Celana Ditambahkan')
    if item == '3':
        price += sepatu
        print('Sepatu Ditambahkan')
    if item == 'selesai':
        print(f'total yang harus anda bayar sebesar Rp.{price}')

print(f'Total yang harus anda bayar sebesar Rp.{price}')

