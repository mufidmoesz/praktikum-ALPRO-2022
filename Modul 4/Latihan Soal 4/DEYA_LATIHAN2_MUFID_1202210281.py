print("================ Rekomendasi Tempat Wisata di Indonesia ================")
class destination:
    def __init__(self, city, julukan, wisata):
        self.city = city
        self.julukan = julukan
        self.wisata =   wisata
    def display(self):
        print(f"Nama Daerah \t: {self.city}\nJulukan \t: {self.julukan}\nTempat Wisata \t: {self.wisata}\n")

reccomend1 = destination('Bandung', 'Kota Kembang', 'Dago Dream Park')
reccomend1.display()

reccomend2 = destination('Bogor', 'Kota Hujan', 'Telaga Warna')
reccomend2.display()

reccomend3 = destination('Yogyakarta', 'Kota Pelajar', 'Candi Prambanan')
reccomend3.display()