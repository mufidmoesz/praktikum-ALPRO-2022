peserta1 = input('Peserta 1, Masukkan sinyal tanganmu : ')
peserta2 = input('Peserta 2, Masukkan sinyal tanganmu : ')
print('Peserta 1, masukkan sinyal tanganmu :', peserta1)
print('Peserta 2, masukkan sinyal tanganmu :', peserta2)

if (peserta1.lower() == 'gunting'):
    if (peserta2.lower() == 'batu'):
        print('Peserta 1 kalah sehingga peserta 2 menang')
    elif (peserta2.lower() == 'kertas'):
        print('Peserta 2 kalah sehingga peserta 1 menang')
    elif (peserta2.lower() == 'gunting'):
        print('Pertandingan seri')
elif (peserta1.lower() == 'batu'):
    if(peserta2.lower() == 'batu'):
        print('Pertandingan seri')
    elif (peserta2.lower() == 'kertas'):
        print('Peserta 1 kalah sehingga peserta 2 menang')
    elif (peserta2.lower() == 'gunting'):
        print('Peserta 2 kalah sehingga peserta 1 menang')
elif (peserta1.lower() =='kertas'):
    if (peserta2.lower() == 'batu'):
        print('Peserta 2 kalah sehingga peserta 1 menang')
    elif (peserta2.lower() == 'kertas'):
        print('Pertanding seri')
    elif (peserta2.lower() == 'gunting'):
        print('Peserta 1 kalah sehingga peserta 2 menang')
else:
    print('Masukkan sinyal tangan yang benar')