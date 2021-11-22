import random
from math import sqrt

def sprLiczbe(n):
    liczba = n
    dzielnik = 2
    poprzedni = 1
    while liczba > 1:
        if liczba % dzielnik == 0:
            if dzielnik == poprzedni:
                return False
            liczba //= dzielnik
            poprzedni = dzielnik
        else:
            dzielnik += 1
    return True

def zad():
    dl = 0
    max_dl = 0
    iloczyn = 1
    n = 0
    while n < len(T):
        iloczyn *= T[n]
        print(iloczyn)
        if not sprLiczbe(iloczyn):
            if max_dl < dl:
                max_dl = dl
            dl = 0
            iloczyn = 1
        else:
            dl += 1
        n += 1
    print(max_dl)


N = 10
# T = [random.randint(1,999) for _ in range(N)]
T = [2,23,33,35,7,4,6,7,5,11,13,22]

zad()