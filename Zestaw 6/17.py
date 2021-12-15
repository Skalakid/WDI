import math

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    if n % 2 ==0:
        return False

    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def rek(n1, n2, result=0, pow=1):
    if n1 == 0 and n2 == 0: # warunek końcowy -> wykożystaliśmy cyfry z obu liczb
        if isPrime(result):
            print(result) # jeśeli pierwsza wypisz i zwróć 1 do ilości liczb pierwszych ( czyli że można podnieść ją o 1 )
            return 1
        return 0 # jeżeli nie pierwsza to zwróć 0 czyli ilość liczb pierwszych się nie zwiększy

    suma = 0

    if n1 > 0:
        suma += rek(n1//10, n2, result + (n1%10) * pow, pow*10) # bierzemy liczbę z n1
    if n2 > 0:
        suma += rek(n1, n2//10, result + (n2 % 10) * pow, pow * 10) # bierzemy liczbę z n2

    return suma

print(rek(123, 75))