def isPal(start, end):
    L = start
    P = end
    while L < P:
        if T[L] != T[P] or T[L] % 2 == 0:
            return False
        L+=1
        P-=1
    return True

def zad(T):
    n = 0
    max_dl = 0
    while n < len(T):
        if T[n] % 2 == 1:
            x = 1
            dl = 0
            while n+x < len(T):
                if isPal(n, n+x):
                    dl = x + 1
                    if max_dl < dl:
                        max_dl = dl
                x += 1
        n += 1
    return max_dl
T = [2,1,3,3,3,1]
print(zad(T))