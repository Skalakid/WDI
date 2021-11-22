import math
def sumaCyfr(n):
    suma = 0
    while n > 0:
        suma += n%10
        n //= 10
    return suma

def isSmithNumber(n):
    suma = 0
    copy_n = n
    d = 2
    while copy_n > 1:
        if copy_n % d == 0:
            suma += sumaCyfr(d)
            copy_n //= d
        else:
            d+=1
    return (suma == sumaCyfr(n))

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# print(rozklad(101))

for i in range(2,1000000):
    if (not isPrime(i)) and isSmithNumber(i):
        print(i)