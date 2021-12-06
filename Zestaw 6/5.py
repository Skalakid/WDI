import math

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def podzial(t, p):
    if p == len(t):
        return True

    a = 0
    index = p
    while index < len(t) and index < 30:
        a = a*2 + t[index]
        print(a)
        if isPrime(a) and podzial(t, index + 1):
            return True
        index += 1
    return False

t = [1,1,1,0,1,1]
print(podzial(t,0))




