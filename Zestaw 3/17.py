from math import sqrt

def toTabBin(n):
    bit = [0 for i in range(len(tab))]
    index = 0
    while n > 0:
        bit[index] = n%2
        n //= 2
        index+=1

    return bit

def isPrime(n):
    for i in range(2, int(sqrt(n))+ 1):
        if n % i == 0:
            return False
    return True

def isInT2(n):
    for i in range(len(t2)):
        if n == t2[i]:
            return True
    return False

def isInT1(n):
    for i in range(len(t1)):
        if n == t1[i]:
            return True
    return False


t1 = [1,3,5,7]
t2 = [11,21,33, 39]
n = len(t1) + len(t2)
tab = t1 + t2
ile = 0
suma = 0
for bin in range(1,2**n):
    bit = toTabBin(bin)
    is_t1_number = False
    is_t2_number = False
    for i in range(n):
        if bit[i] == 1:
            suma += tab[i]
            if i < n//2:
                is_t1_number = True
            elif i >= n//2:
                is_t2_number = True

    if isPrime(suma) and is_t1_number and is_t2_number:
        ile += 1
    suma = 0
    bit = []

print(ile)