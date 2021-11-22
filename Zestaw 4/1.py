N = int(input())
T = [[0 for i in range(N)] for j in range(N)]
i = 0
j = 0
index = (N*N)-1
T[0][0]=index+1
czyMoznaPrawo=True
while index > 0:
    print(i,j)
    if j + 1 < N and T[i][j+1] == 0 and czyMoznaPrawo:
        T[i][j + 1] = index
        index-=1
        j+=1
    elif i + 1 < N and T[i+1][j] == 0:
        czyMoznaPrawo = False
        T[i+1][j] = index
        index-=1
        i+=1
    elif j - 1 >= 0 and T[i][j-1] == 0:
        T[i][j - 1] = index
        index-=1
        j-=1
    elif i - 1 >= 0 and T[i-1][j] == 0:
        T[i - 1][j] = index
        index-=1
        i-=1
    else:
        czyMoznaPrawo = True

for i in range(len(T)):
    print(T[i])