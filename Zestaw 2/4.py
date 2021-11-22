
def checkNumber(n):
    d = 2
    while n > 1:
        if d > 5:
            return False
        if n % d == 0:
            n //= d
        else:
            d += 1
    return True

N = int(input())
suma = 1
for i in range(2,N):
    if checkNumber(i):
        suma += 1
print(suma)