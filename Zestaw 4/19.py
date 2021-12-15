iloczyn = int(input())

ruchy = ((1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2))
N = 8
T = [[i for _ in range(N)] for i in range(N)]
for i in range(N):
    print(T[i])



ile = 0
for y in range(N):
    for x in range(N):

       for ruch in ruchy:
           if 0<=y+ruch[0]<N and 0<=x+ruch[1]<N:
               if T[y][x]*T[y+ruch[0]][x+ruch[1]] == iloczyn:
                   ile+=1

print(ile/2)