line = int(input('Masukkan tinggi baris : '))

n = 0
for i in range(line):
    space = ''
    for j in range(n):
        space += ' '
    
    print(f'{space}*')
    n = n + 1