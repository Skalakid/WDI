import math
import random
import sys
sys.setrecursionlimit(15000)

def odl(y1, x1, y2, x2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def firstDigit(n):
    if n < 10:
        return n
    return n // 10**(int(math.log10(n)))

def printTab(T):
    for i in range(len(T)):
        for j in range(len(T)):
            print(T[i][j], end="\t")
        print('')
    print()

def king(T, path, cel_y, cel_x, y=0, x=0, ruch=0):
    ruchy = ((0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1))

    # printTab(path)

    if y == cel_y and x == cel_x:
        path[y][x] = "R"
        print("Cel:", cel_y, cel_x)
        printTab(path)
        sys.exit()

    for i in range(len(ruchy)):
        if 0 <= y + ruchy[i][0] < 8 and 0 <= x + ruchy[i][1] < 8 and firstDigit(T[y + ruchy[i][0]][x + ruchy[i][1]]) > T[y][x]%10 and path[y + ruchy[i][0]][x + ruchy[i][1]] == "-":
                path[y][x] = i
                # print(y, x)
                if odl(y + ruchy[i][0], x + ruchy[i][1], cel_y, cel_x) <= odl(y,x,cel_y, cel_x):
                    king(T, path, cel_y, cel_x, y + ruchy[i][0], x + ruchy[i][1], ruch+1)
    path[y][x] = "-"
    return

T = [[random.randint(10, 100) for _ in range(8)] for i in range(8)]
path = [["-" for _ in range(8)] for i in range(8)]

# T = [
#     [21,101,10,	10,	10,	10,	10,	21]	,
#     [21,21,21,	21,	10,	21,	21,	21]	,
#     [10,12,	12,	21,	12,	12,	12,	12]	,
#     [10,13,	13,	21,	13,	13,	13,	13]	,
#     [10,14,	14,	21,	21,	21,	14,	14]	,
#     [10,15,	15,	15,	15,	15,	21,	15]	,
#     [10,16,	16,	16,	16,	16,	16,	21],
#     [10,17, 17, 17,	17,	17,	17,	21]
# ]

printTab(T)
king(T, path, 0,7, 0, 0)
king(T, path, 7,7, 0, 0)
king(T, path, 7,0, 0, 0)

