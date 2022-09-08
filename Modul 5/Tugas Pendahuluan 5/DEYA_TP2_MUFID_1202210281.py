from collections import Counter


number = []
banyakAngka = int(input("Masukkan banyak angka: "))
for i in range(banyakAngka):
    number.append(int(input("Masukkan angka: ")))

number.sort()
print([item for item, count in Counter(number).items() if count >= 1])