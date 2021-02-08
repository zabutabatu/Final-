sayilar = [1,5,29,35,85,6,101,26]
print(max(sayilar))

bs = 0
for s in sayilar:
    if s > bs:
        bs = s

print("En büyük sayı bu kardeş:",bs)