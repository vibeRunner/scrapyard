#by M81V4N
#v3.0 'SonicPrimes'
import math

#temporary
a = float(9)
primes = [2, 3, 5, 7]

#main loop
while True:
    #clear
    search = 0
    choosenOnes = []
    root = math.sqrt(a)

    #divides and tests
    while True:
        calcFloat = float(a / primes[search])
        calcInt = int(calcFloat)

        if calcFloat == calcInt:
            choosenOnes.append(primes[search])
            break

        search += 1

        if root < primes[search]:
        	break

    #appears
    if len(choosenOnes) == 0:
        print(int(a))
        primes.append(a)

    a += 2
