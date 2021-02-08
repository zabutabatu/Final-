sayilar = [ 25,86,32,4,2]
print(sayilar[: : -1])

ters = []
for i in range(len(sayilar)-1,-1,-1):
    ters.append(sayilar[i])

print(ters)