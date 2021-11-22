import math


def czyPal(n, base):
    copy_n = n
    rev = 0
    len_n=int(math.log10(n))+1
    iter = len_n-1
    while copy_n > 0:
        rev =(rev*base) + (copy_n % base)
        copy_n //= base

    if rev == n:
        return True
    return False

n = int(input())
print(czyPal(n, 10))
print(czyPal(n, 2))