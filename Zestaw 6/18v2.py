import math
from random import randint

# T = [[randint(0, 99) for _ in range(8)] for _ in range(8)]
T = [[i for j in range(8)] for i in range(8)]
N = len(T)


def first_digit(number):
    if number < 10:
        return number
    return number // pow(10, int(math.log10(number)))

def place_king(y=0, x=0, p_y=0, p_x=0, path=[]):

    if y == N-1 and x == N-1:
        path.append((y, x))
        print(path)
        return True

    # print(y >= N, x >= N)
    if y > N-1 or x >= N-1 or p_y >= N-1 or p_x >= N-1:
        return False
    else:
        print(y, x)
        if first_digit(T[y][x]) < T[p_y][p_x] % 10:
            return False

    p = path[:]
    p.append((y,x))
    return place_king(y, x+1, y, x, p) or place_king(y+1, x, y, x, p) or place_king(y+1, x+1, y, x, p)

def wypiszT(T):
    for i in range(8):
        for j in range(8):
            print(T[i][j], end="\t")
        print('')
    print()

wypiszT(T)
print(place_king())