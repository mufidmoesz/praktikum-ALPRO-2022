print('===Selama Datang Di Kalkulator Sederhana===')

bilangan1 = int(input('masukkan bilangan 1'))
bilangan2 = int(input('masukkan bilangan 2'))
operator = input('masukkan operasinya (+ -)')

print('Masukkan bilangan 1 :', bilangan1)
print('Masukkan operasinya :', operator)
print('Masukkan bilangan 2 :', bilangan2)

match operator:
    case '+':
        result = bilangan1 + bilangan2
    case '-':
        result = bilangan1 - bilangan2
    case _:
        print('Masukkan operator + atau - untuk menghitung bilangan')

print('Hasil Operasi', bilangan1,operator,bilangan2, '= ', result)
