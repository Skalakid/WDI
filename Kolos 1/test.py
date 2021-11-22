import math

def czyPotega(n):
    for i in range(2,n):
        if (math.pow(n, 1/i))%1 == 0:
            return True
    return False

def suma_el(t, L, P):
    suma = 0
    for i in range(L,P):
        suma += t[i]
    return suma





def zad(t1, t2):
    if 2*len(t1) < 24:
        return False
    n = 0
    suma_t1 = 0
    suma_t2 = 0
    while n < len(t1):
        x = 1
        while n+x <= len(t1):
            # print(t1[n:n+x], suma_el(t1,n,n+x), x)
            suma_t1 = suma_el(t1,n,n+x)
            m = 0
            while m < len(t2):
                y = 24 - x
                if m + y <= len(t2):
                    suma_t2 = suma_el(t2, m, m + y)
                    # print("  t2", t2[m:m + y], suma_el(t2, m, m + y), y)
                    if czyPotega(suma_t1 + suma_t2):
                        return True
                m += 1
            x+=1
        n+=1
    return False

t1 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
t2 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
print(zad(t1,t2))






