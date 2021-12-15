def odwaz(T, m, i=0, masa=0):
    if i == len(T)-1:
        return masa + T[i] == m or masa == m
    return odwaz(T, m, i+1, masa + T[i]) or odwaz(T, m, i+1, masa)

T = [1,2,3,4]
m = int(input())
print(odwaz(T,m))
