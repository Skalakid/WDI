import random


def sumujWiesz(i):
    suma = 0
    for liczba in T[i]:
        suma += liczba
    return suma

def sumujKolumne(j):
    suma = 0
    for i in range(N):
        suma += T[i][j]
    return suma

def sprTablice(T):
    maxIloraz = 0
    max_i = 0
    max_j = 0
    for i in range(N):
        for j in range(N):
            # print(sumujKolumne(j),'/',sumujWiesz(i),sumujKolumne(j)/sumujWiesz(i))
            iloraz = sumujKolumne(j)/sumujWiesz(i)
            if maxIloraz < iloraz:
                maxIloraz = iloraz
                max_i = i
                max_j = j
    return max_j,max_i


N = 5
T = [[random.randint(1, 9) for i in range(N)] for j in range(N)]
for i in range(N):
    print(T[i])
print(sprTablice(T))


wiersze = [sumujWiesz(i) for i in range(N)]
kolumny = [sumujKolumne(i) for i in range(N)]
for i in range(N):
    if wiersze[i] == min(wiersze):
        max_wier = i
    if kolumny[i] == max(kolumny):
        max_kol = i
print(max_kol,max_wier)