def sumaOtoczenia(T, y, x):
    ruchy = ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1))
    suma = 0
    for poz in ruchy:
        if 0<=y+poz[0]<len(T) and 0<=x+poz[1]<len(T):
            suma+=T[y+poz[0]][x+poz[1]]

    return suma

def spr(T):
    max_suma = 0
    poz = ()
    for y in range(len(T)):
        for x in range(len(T)):
            suma = sumaOtoczenia(T,y,x)
            if max_suma < suma:
                max_suma = suma
                poz = (y,x)

    return poz

N = 12
T = [[i for _ in range(N)] for i in range(N)]
for i in range(N):
    print(T[i])

print(spr(T))

