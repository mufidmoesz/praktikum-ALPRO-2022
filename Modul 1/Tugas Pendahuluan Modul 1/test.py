print ('=== Hasil Penjualan PT. Perindro ===')

Semen = int(input('masukkan hasil penjualan semen bulan ini :'))
Batubata = int(input('masukkan hasil penjualan batu bata bulan ini :'))
Paku = int(input('masukkan hasil penjualan paku bulan ini :'))

jumlahdata = Semen + Batubata + Paku
ratarata = jumlahdata / 3

print ('Hasil penjualan semen bulan ini\t:\t', Semen)
print ('Hasil Penjualan batu bata bulan ini\t:\t', Batubata)
print ('hasil penjualan paku bulan ini\t:\t', Paku)
print ('Rata-rata hasil penjualan bulan ini: ', ratarata)
