import math


def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    if n % 2 ==0:
        return False

    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def rek(n, i=1, num_of_parts=0):
    if isPrime(num_of_parts) and isPrime(n):
        return True

    if i > n:
        return False

    if isPrime(n % i):
        if rek(n//i,10, num_of_parts+1):
            return True

    return rek(n, 10*i, num_of_parts)

print(rek(222))