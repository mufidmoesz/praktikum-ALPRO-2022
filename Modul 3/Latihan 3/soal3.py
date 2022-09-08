for i in range(1, 16):
    if i%3 == 0 and i%5 == 0:
        print('PawPow')
    elif i%3 == 0:
        print('Paw')
    elif i%5 == 0:
        print('Pow')
    else:
        print(i)