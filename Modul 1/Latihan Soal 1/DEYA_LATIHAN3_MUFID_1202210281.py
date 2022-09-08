print('===PROGRAM INPUT NILAI===')

nama = input('masukkan nama anak didik')
nilai_membaca = int(input('masukkan nilai membaca'))
nilai_berhitung = int(input('masukkan nilai berhitung'))

print('Nama Anak Didik : ', nama)
print('Nilai Membaca = ', nilai_membaca)
print('Nilai Berhitung = ', nilai_berhitung)

index = (nilai_membaca + nilai_berhitung) / 2

if index >= 90 and index <= 100:
    print('Indeks nilai A : True')
else:
    print('Indeks nilai A : False')
