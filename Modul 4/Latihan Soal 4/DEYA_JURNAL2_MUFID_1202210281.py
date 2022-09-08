class Band:
    def __init__(self, name, member, genre):
        self.name = name
        self.member = member
        self.genre = genre

    def display(self):
        if self.genre.lower() == "indie":
            print("Cari studio lain broo")
        else:
            print("lu punya band asik banget")

name = input("Masukkan nama band : ")
member = int(input("Masukkan jumlah anggota band : "))
genre = input("Masukkan genre band anda : ")

obj = Band(name, member, genre)
obj.display()