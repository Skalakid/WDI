def czy_iloczyn_2_pierwszych(n):
    ile = 0
    d = 2
    while n > 1:
        if ile == 2:
            return False
        if n % d == 0:
            n //= d
            ile += 1
        else:
            d+=1
    if ile == 2:
        return True
    return False

def suma_el(t, L, P):
    suma = 0
    for i in range(L,P):
        suma += t[i]
    return suma

def zad(t1, t2):
    n = 0
    while n < len(t1):
        x = 1
        while n+x <= len(t1):
            suma_t1 = suma_el(t1,n,n+x)
            m = 0
            while m < len(t2):
                y = x
                if m + y < len(t2):
                    suma_t2 = suma_el(t2, m, m+y)
                    if czy_iloczyn_2_pierwszych(suma_t1+suma_t2):
                        print(suma_t1+suma_t2)
                        return True
                m+=1
            x+=1
        n+=1
    return False


t1 = [1,1,1,1,1,1]
t2 = [1,1,1,1,1,1]
print(zad(t1,t2))


