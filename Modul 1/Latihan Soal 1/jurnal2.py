print('===Harga Skincare===')

skinwhitening = 670000
skinultimateseries = 880000
skinacneseries = 450000

whitening = int(input('jumlah skincare whitening'))
ultimateseries = int(input('jumlah skincare ultimate series')) 
acneseries = int(input('jumlah skincare acne series'))

print('Harga Skincare Whitening = ', skinwhitening)
print('Harga Skincare Ultimate Series = ', skinultimateseries)
print('Harga Skincare Acne Series = ', skinacneseries)

totalharga = (skinwhitening*whitening)+(skinultimateseries*ultimateseries)+(skinacneseries*acneseries)

if ultimateseries >= 1:
    diskon = totalharga * (30/100)
    hargadiskon = totalharga - diskon
if whitening >= 1:
    diskon2 = hargadiskon * (50/100)
    hargadiskon2 = hargadiskon - diskon2
    print('Total Harga = ', hargadiskon2)
