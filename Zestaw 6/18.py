import math
import random
import sys


def krol(k, w):
    ruchy = ((1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1))
    global T
    # print("skok", w, k)
    if w == 7 and k == 7:
        print("Mamy to")
        sys.exit()
        return True

    for ruch in ruchy:
        if 0 <= w + ruch[1] < 8 and  0 <= k + ruch[0] < 8:
            # print(k + ruch[0], w + ruch[1], odlegloscOdMety(w + ruch[1], k + ruch[0]))
            if odlegloscOdMety(w + ruch[1], k + ruch[0]) < odlegloscOdMety(w, k):
                next = T[k + ruch[0]][w + ruch[1]]


                if int(math.log10(next))+1 == 1:
                    pierwszaCyfra = next
                else:
                    pierwszaCyfra = next // pow(10, int(math.log10(next)))
                if (T[k][w])%10 < pierwszaCyfra:
                    krol(k + ruch[0], w + ruch[1])

    return False

def odlegloscOdMety(x1, y1):
    return math.sqrt((x1-7)**2 + (y1-7)**2)

def wypiszT(T):
    for i in range(8):
        for j in range(8):
            print(T[i][j], end="\t")
        print('')
    print()


# T = [[random.randint(10, 20) for _ in range(8)] for _ in range(8)]
T = [[i for j in range(8)] for i in range(8)]
wypiszT(T)
print(odlegloscOdMety(6,7))
print()
print(krol(0,0))