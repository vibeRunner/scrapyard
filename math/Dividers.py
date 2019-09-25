#by M81V4N
print('Dividers Finder v.1.0 by M81V4N')
a = input('num:  ')
a = float(a)
ad = []


search = 1
calc = 0
intcalc = 0

while True:
    calc = (a/search)
    intcalc = int(calc)
    if calc == intcalc:
        if intcalc not in ad:
            ad.append(intcalc)
        if calc == 1:
            break
    search += 1

print("\n")
print(ad)

if len(ad) == 2 or len(ad) == 1:
    print("PRIME NUMBER!")
