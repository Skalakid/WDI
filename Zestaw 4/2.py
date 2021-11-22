import math
import random

def czySameCyfryNP(n):
    if n%2==0: return False
    for i in range(int(math.log10(n))+1):
        if (n%10)%2==0:
            return False
        n//=10
    return True

def sprTablice(T):
    i = 0
    while i < N:
        czyNPwWierszu = False
        for j in range(N):
            if czySameCyfryNP(T[i][j]):
                czyNPwWierszu=True
                break
        if not czyNPwWierszu:
            return False
        i+=1
    return True

N = 1
T = [[random.randint(100, 999) for i in range(N)] for j in range(N)]
print(T)
print(sprTablice(T))