import random

def sprTablice(T):
    i = 0
    while i < N:
        czySameParzyste = True
        for liczba in T[i]:
            if liczba%2 == 1:
                czySameParzyste=False
                break
        if czySameParzyste:
            return True
        i +=1
    return False




N = 3
T = [[random.randint(100, 999) for i in range(N)] for j in range(N)]
print(T)
print(sprTablice(T))