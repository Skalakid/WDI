import math
import random


def isPrime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True

    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def zad13(T):
    for i in range(len(T)):
        for j in range(len(T)):
            flag = False
            for y in range(len(T)):
                for x in range(len(T)):
                    if T[y][x] == 0: continue
                    if y != i or x != j:
                        if isPrime(T[i][j] + T[y][x]):
                            flag = True
                            break
                if flag:
                    break
            if not flag:
                T[i][j] = 0

    return T

T = [[3 for i in range(4)] for i in range(4)]
print(zad13(T))