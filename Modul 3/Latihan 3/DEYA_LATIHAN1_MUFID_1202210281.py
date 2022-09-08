print('--------Silahkan Login---------')

attempt = 3
while True:
    username = input('Masukkan username : ')
    password = input('Masukkan password : ')

    if username == 'qwerty' and password == 'kijolp':
        print('Anda berhasil login')
        break
    else:
        print(f'Gagal login, {attempt} percobaan tersisa')
        attempt -= 1
        if attempt == -1:
            break
