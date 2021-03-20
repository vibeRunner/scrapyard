#by M81V4N
#split number on prime numbers
import math
num = int(input("num: "))
print()

containsPrimes = []
currentNum = num
dividers = []
killTheInfiniteLoopOfDoom = False
longestLen = 0
a = float(5)
primes = [2, 3]


#generate primes smaller than num
while True:
    #clear
    search = 0
    choosenOnes = []
    root = math.sqrt(a)
    
    while True:
        calcFloat = float(a / primes[search])
        calcInt = int(calcFloat)
        if calcFloat == calcInt:
            choosenOnes.append(primes[search])
            break
        search += 1
        if root < primes[search]:
            break
            
    if len(choosenOnes) == 0:
        primes.append(int(a))
        
    if a >= num:
      break
    
    a += 2

    
if primes[-1] == num:
    print(str(num)+' | '+str(num))
    print('PRIME NUMBER')
    dividers.append(nim)
    
    
else:
    longestLen = len(str(num))
    while True:
        for a in primes:
            if currentNum/a == int(currentNum/a):
                print((longestLen - len(str(currentNum))) * ' ' +str(currentNum)+ ' | ' +str(a))
                currentNum = int(currentNum/a)
                dividers.append(a)
                break
                
            if currentNum == 1:
            	killTheInfiniteLoopOfDoom = True
            	print((longestLen - len(str(currentNum))) * ' ' +"1 |")
            	break
        
        if killTheInfiniteLoopOfDoom is True:
            break
             
              
