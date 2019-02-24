#by M81V4N

#temporary
a = float(9)
primes = [2, 3, 5, 7]

#main loop
while True:
    #clear
    search = 0
    choosenOnes = []

    #divides and tests
    while True:
        calcFloat = float(a / primes[search])
        calcInt = int(calcFloat)

        if calcFloat == calcInt:
            choosenOnes.append(primes[search])

        if search == len(primes) - 1:
            break

        if len(choosenOnes) > 0:
            break

        search += 1

        if a/2 <= primes[search]:
        	break

    #appears
    if len(choosenOnes) == 0:
        print(int(a))
        primes.append(a)

    a += 2
