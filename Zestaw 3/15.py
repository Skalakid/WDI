from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def zad():
    ppop = 1
    pop = 1
    n = 1
    czyPierwszaWPozostalych = False
    if isPrime(T[0]):
        return False

    while n < len(T):
        print(pop)
        if n == pop:
            if isPrime(T[pop]):
                return False
            pop,ppop = pop+ppop,pop
        else:
            if isPrime(T[n]):
                czyPierwszaWPozostalych = True
        n+=1

    if czyPierwszaWPozostalych:
        return True
    return False



T = [4,4,4,4,2]
print(zad())