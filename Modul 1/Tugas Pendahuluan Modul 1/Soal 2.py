import statistics


print ('=== Hasil Penjualan PT. Perindro ===')

semen = int(input('masukkan hasil penjualan semen bulan ini :'))
batubata = int(input('masukkan hasil penjualan batu bata bulan ini :'))
paku = int(input('masukkan hasil penjualan paku bulan ini :'))

data = ((semen),(batubata),(paku))

ratarata = statistics.mean(data)

print ('Hasil penjualan semen bulan ini\t:\t', semen)
print ('Hasil Penjualan batu bata bulan ini\t:\t', batubata)
print ('hasil penjualan paku bulan ini\t:\t', paku)
print('Rata-rata hasil pejualan bulan ini :', ratarata)