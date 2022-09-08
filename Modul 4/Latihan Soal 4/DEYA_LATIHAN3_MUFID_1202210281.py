def sifatWakhid(jodoh, wakhid = "wibu"):
    if jodoh == wakhid:
        print("Wakhid dan jodoh cocok")
    else:
        print("Wakhid dan Jodoh tidak cocok")

jodoh = input("Masukkan sifat calon jodoh: ")
sifatWakhid(jodoh.lower())