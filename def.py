def faktor(a):
    f = 1
    for b in range(2, a+1):
        f *= b
    return f

sonuc = faktor(5)
print(sonuc)

def carp(sayi1, sayi2):
    return sayi1 * sayi2

print(carp(10,11))