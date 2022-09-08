line = int(input('Masukkan tinggi baris : '))

for i in range(line):
    for j in range(i + 1):
        if i == j:
            print('*', end=' ')
        else:
            print(end=' ')
    print('') 