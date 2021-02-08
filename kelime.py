import random

sayilar = []
maks = 150
for i in range(5):
    sayi = random.randrange(1,maks)
    while sayi in sayilar:
        print("Eee bu aynısı geldi ben değiştirdim hocam")
        sayi = random.randrange(1,maks)

    sayilar += [sayi]

print(sayilar)