print("|| Program Tantangan Mr. X ||")

name = input("Masukkan nama : ")
id = input("Masukkan ID : ")
division = input("Masukkan divisi : ")
status = input("Masukkan status : ")

file = open('tantangan.txt', 'w')

file.write(f"Halo, perkenalkan namaku {name} dengan NIM {id} dan berada di kelas {division}. Status hubunganku saat ini {status}. hehehe <3")