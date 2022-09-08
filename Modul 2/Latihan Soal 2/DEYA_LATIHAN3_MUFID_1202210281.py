print('==== Menu ====')

pintujendela = 1
cctv = 2
alarm = 3

pilihan = int(input('Masukkan pilihan anda : '))

match pilihan:
    case 1:
        print('1. Kunci\n2. Buka kunci')
        pilihan1 = int(input('Masukkan pilihan anda (1 atau 2) : '))
        if pilihan1 == 1:
            print('Pintu dan jendela telah terkunci')
        elif pilihan1 == 2:
            print('Kunci pintu dan jendela telah terbuka')
    case 2:
        print('1. Nyalakan\n2. Matikan')
        pilihan2 = int(input('Masukkan pilihan anda (1 atau 2) : '))
        if pilihan2 == 1:
            print('CCTV anda telah dinyalakan')
        elif pilihan2 == 2:
            print('CCTV anda telah dimatikan')
    case 3:
        print('1. Nyalakan\n2. Matikan')
        pilihan3 = int(input('Masukkan pilihan anda (1 atau 2) :'))
        if pilihan3 == 1:
            print('Alarm anda telah dinyalakan')
        elif pilihan3 == 2:
            print('Alarm anda telah dimatikan')
    case _:
        print(f'Pilihan {pilihan} tidak ada')