from statistics import mean


jumlahmurid = int(input('masukkan jumlah muridnya : '))

data = []
for i in range(1, jumlahmurid + 1):
    nilaimurid = int(input('masukkan nilai murid ke-'+ str(i) +': '))
    data.append(nilaimurid)
    
ratarata = mean(data)
print(f'nilai rata rata {jumlahmurid} murid tersebut adalah {ratarata} ')