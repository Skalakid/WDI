import math

def convert(T):
    num = 0
    pow = 0
    for i in range(len(T)-1, -1, -1):
        if T[i] == 1:
           num += 2 ** pow
        pow += 1

    return num

def isPrime(n):
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def wrapper(A, B):
    T = [0 for _ in range(A+B)]
    T[0] = 1
    return rek(T, 1, A-1, B)


def rek(T, i, A, B):
    if i == len(T):
        if not isPrime(convert(T)):
            print(T)
            return 1
        return 0

    suma = 0
    if A > 0:
        T[i] = 1
        suma += rek(T, i + 1, A-1, B)
    if B > 0:
        T[i] = 0
        suma += rek(T, i + 1, A, B - 1)

    return suma



print(wrapper(2, 4))