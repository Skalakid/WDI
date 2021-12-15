def det(T):
    if len(T) == 1:
        return T[0][0]

    suma = 0
    d = 0
    for i in range(len(T)):
        print((-1)**d, '*', T[0][i], '*', shrinkTab(T, i))
        suma += (-1)**d * T[0][i] * det(shrinkTab(T, i))
        d+=1

    return suma

def shrinkTab(T, row):
    new_T = [[0 for _ in range(len(T) - 1)] for _ in range(len(T) - 1)]
    y, x = 0, 0
    for i in range(len(T)):
        if i == 0: continue
        for j in range(len(T)):
            if j == row: continue
            new_T[y][x] = T[i][j]
            x += 1
        if x == len(T) - 1:
            x = 0
            y += 1
    return new_T


T = [
    [12, 3, 4, 4],
    [2, 2, 4, 4],
    [5, 3, 1, 4],
    [1, 1, 1, 1]
]
print(det(T))

