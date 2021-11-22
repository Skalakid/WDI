def zad():
    max_el = 0
    for i in range(N):
        for j in range(N):
            if T1[i][j] > max_el:
                max_el = T1[i][j]

    T3 = [0 for _ in range(max_el+1)]
    for i in range(N):
        for j in range(N):
            T3[T1[i][j]] += 1

    index = 0
    for i in range(len(T3)):
        if T3[i] == 1:
            T2[index] = i
            index+=1
    print(T2)



N = 4
T1 = [
    [1,2,3,4],
    [4,5,5,9],
    [3,5,8,9],
    [6,6,7,7]
]
T2 = [0 for _ in range(N*N)]

zad()