nim = "1202210281"
password = "PestaRahasiaNihBos"

try:
    nimInput = input("Masukkan kode NIM mu : ")
    pwInput = input("Masukkan password mu : ")

    try:
        if len(pwInput) >= 8:
            if nimInput == nim and pwInput == password:
                print("Silakan masuk")
            else:
                print("Kode NIM atau Password salah!")
        else:
            raise NameError
    except NameError:
        print("Password harus lebih dari 8 karakter!")
except ValueError:
    print("Kode NIM atau password salah!")
