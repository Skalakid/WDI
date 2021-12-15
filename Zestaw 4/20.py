N = 8
T = [[i for _ in range(N)] for i in range(N)]
for i in range(N):
    print(T[i])

wieze = [None for i in range(N)]

best_suma = 0
x_y = ()
for i in range(N):
    for j in range(N):
        wieze[i] = j
        for y in range(N):
            if y == i: continue
            for x in range(N):
                if x == j:
                    continue
                suma = T[i][j] + T[y][x]
                if suma > best_suma:
                    best_suma = suma
                    x_y = ((i,j), (y,x))

print(x_y)