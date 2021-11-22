def rozklad(n):
    t = [None for _ in range(n)]
    d = 2
    index = 0
    while n > 1:
        if n % d == 0:
            n //= d
            if not d in t:
                t[index] = d
                index += 1
        else:
            d+=1
    return t[:index]

def jazda():
    t_bool = [0 for i in t]
    t_bool[0] = 1
    for i in range(len(t)):
        if t_bool[i] == 1:
            d = 2
            while t[i] > 1:
                if t[i] % d == 0:
                    t[i] //= d
                else:
                    d += 1
                if i + d < len(t):
                    t_bool[i + d] = 1
    print(t_bool)
    return  t_bool[-1]




t = [6, 3, 2, 3, 3, 1]
print(jazda())