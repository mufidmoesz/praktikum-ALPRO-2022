name = "Muhammad Mufid Musyaffa"
kelas = "SI-45-03"
nim = "1202210281"
motto = "Kepribadianmu adalah kunci kehidupanmu"

with open('Tambahin.txt', 'a') as f:
    f.write(f"Nama : {name}\n")
    f.write(f"Kelas : {kelas}\n")
    f.write(f"NIM : {nim}\n")
    f.write(f"Motto : {motto}\n")
