def A(n):
    return n+3

def B(n):
    return 2*n

def C(n):
    pow = 1
    copy_n = n

    while copy_n > 0:
        cyfra = copy_n % 10
        if cyfra % 2 == 0:
            n += 1*pow
        pow*=10
        copy_n //= 10

    return n


def rek(X, Y, N, i=0, last="X"):
    if X == Y:
        return 1

    if i >= N:
        return 0

    suma = 0
    if last != "A":
        suma += rek(A(X),Y,N,i+1,"A")
    if last != "B":
        suma += rek(B(X),Y,N,i+1,"B")
    if last != "C":
        suma += rek(C(X),Y,N,i+1,"C")


    return suma


print(rek(11,31,4))