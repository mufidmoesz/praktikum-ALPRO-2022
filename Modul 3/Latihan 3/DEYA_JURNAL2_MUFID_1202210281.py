from statistics import mean


print('=== Program Perhitungan Tinggi badan Infinity===')
print("ketik 'stop' untuk menghentikan perulangan")

data = []
order = 1
while True:
    height = input(f'Masukkan tinggi orang ke-{order} : ')
    if height == 'stop':
        
        average = mean(data)
        break
    else:
        data.append(int(height))
        order = order + 1

print(f'Rata-rata tinggi badan adalah {average}')