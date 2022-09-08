print('========== Daspro Market==========')

list = []
def trolly(x):
    return list.append(x)

while True:
    print('Ketik stop untuk berhenti')
    item = input('Masukkan nama barang ke dalam keranjang : ')
    if item.lower() == 'stop':
        break
    else:
        trolly(item)

print('Barang yang berada didalam keranjang :',', '.join(list))