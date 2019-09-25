# by M81V4N
# github.com/M81V4N

import math as m

print("PascalBracket v1.0")
print("works on python 2.x")
print("(A+B)/\\M")
print("M can be only above 0")
print("You can make B substracting by putting '-' in front of it")
print("You can make roots by writing  x**(1/float(n))")
varA = input("A part: ")
varB = input("B part: ")
multi = input("Multi: ")

now = []
prev = []
while len(now)-1 != multi:
    now = [1]
    for a in range(1,len(prev)+1):
        try:
            now.append(prev[a-1]+prev[a])
        except:
            now.append(1)
            break
    prev = now
    
forceA = 1
for a in now:
    if a > forceA:
        forceA = a
forceB = 0

final = 0
for a in now:
    final += a*varA**forceA*varB**forceB
    forceA -= 1
    forceB += 1
    
print(final)
