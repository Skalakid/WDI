T =  [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)]
def longest(T):

    q = 1
    if (T[0][0]/T[0][1]) != 0:
        q = (T[1][0]/T[1][1])/(T[0][0]/T[0][1])

    dl = 2
    max_dl = 0
    for i in range(2, len(T)):
        print(q)
        if q == (T[i][0]/T[i][1])/(T[i-1][0]/T[i-1][1]):
            dl += 1
        else:
            dl = 2
            q = (T[i][0] / T[i][1]) / (T[i - 1][0] / T[i - 1][1])

        if max_dl < dl:
            max_dl = dl
    if max_dl == 2:
        return 0
    return max_dl

print(longest(T))