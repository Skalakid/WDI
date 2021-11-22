def checkRev(L,P):
    n = len(t)-1
    copy_L = L
    while n > P:
        if t[n] == t[copy_L]:
            while copy_L <= P:
                if t[n] == t[copy_L]:
                    copy_L += 1
                    n -= 1
                else:
                    break
            else:
                return True
        n -= 1
    return False

def zad():
    max_dl = 0
    n = 0
    while n < len(t)//2:
        x = 1
        while n+x < len(t)//2:
            dl = 0
            print(t[n:n+x+1], checkRev(n,n+x), x+1)
            if checkRev(n,n+x):
                dl = x+1
            if max_dl < dl:
                max_dl = dl
            x+=1
        n+=1
    return max_dl


t = [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
print(zad())