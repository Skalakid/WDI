import math

def zad(n):
    len_n = int(math.log10(n))+1
    while n > 0:
        if n%10 == len_n:
            return True
        n //= 10
    return False


n = int(input())
print(zad(n))