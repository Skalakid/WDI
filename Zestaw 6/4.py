
def skoczek(t, y, x, nr_skoku=1):
    t[y][x] = nr_skoku

    if nr_skoku == len(t)**2:
        printBoard(t)
        return True
    else:
        jumps = ((-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1))
        for jump in jumps:
            if 0 <= y + jump[0] < len(t) and 0 <= x + jump[1] < len(t) and t[y + jump[0]][x + jump[1]] == 0:
                if skoczek(t, y + jump[0], x + jump[1], nr_skoku+1):
                    return True
        t[y][x] = 0
    return False

def printBoard(t):
    for i in range(len(t)):
        for j in range(len(t)):
            print(t[i][j], end='\t')
        print('')
    print()

n = int(input())
t = [[0 for _ in range(n)] for _ in range(n)]
for i in range(len(t)):
        for j in range(len(t)):
            skoczek(t, i, j)