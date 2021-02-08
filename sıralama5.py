asal = [2,3]
limit = 50
for i in range(5,limit +1,2):
    bolundu = False
    for a in asal:
        if i%a ==0 :
            bolundu = True
            break
        if not bolundu:
            print("Al sana asal sayı kanki{}".format(i))
            asal += [i]

print(asal)