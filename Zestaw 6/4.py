# Problem skoczka
import sys
stop = False

def skok(arr, y, x, nr_ruchu = 1):
    global stop

    # printChess(arr)
    # print()

    if stop:
        return

    arr[y][x] = nr_ruchu

    if nr_ruchu == n*n:
        printChess(arr)
        return True
    else:
        jumps = ((-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1))
        for jump in jumps:
            if -1 < y + jump[0] < len(arr) and -1 < x + jump[1] < len(arr) and arr[y + jump[0]][x + jump[1]] == 0:
                if skok(arr, y + jump[0], x + jump[1], nr_ruchu + 1):
                    return True
        arr[y][x] = 0
    return False

def printChess(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end='\t')
        print('')
    print()

def clearTab(t):
    for i in range(len(t)):
        for j in range(len(t)):
            t[i][j] = 0


n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
flaga = False
for i in range(n):
    for j in range(n):
        clearTab(arr)
        if skok(arr,i,j,1):
            flaga = True
            break
    if flaga:
        break
if not flaga:
    print(False)

