import math


def convertToBin(n):
    converted = 0
    pow = 0
    while n > 0:
        if n % 2 == 1:
           converted += 10**pow
        n //=2
        pow += 1
    return converted

def num_of_ones(n):
    ones = 0
    while n > 0:
        if n % 10 == 1:
            ones += 1
        n//=10
    return ones

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) +1):
        if n % i == 0:
            return False
    return True

def zad(a,b):
    len_a = int(math.log10(a))+1
    len_b = int(math.log10(b))+1
    len_c = len_b + len_a
    repeat_check = 1
    suma = 0
    for i in range(2**(len_c), 2**(len_c+1)):
        new_number = 0
        mask = convertToBin(i)

        if (num_of_ones(mask)-1) != len_b:
            continue
        copy_a = a
        copy_b = b
        iter = 0
        while mask != 1:
            if mask % 10 == 0:
                new_number += (copy_a % 10) * 10**iter
                copy_a //= 10
            else:
                new_number += (copy_b % 10) * 10**iter
                copy_b //= 10
            iter += 1
            mask //= 10
        print(new_number, isPrime(new_number))
        if repeat_check % new_number != 0:
            if isPrime(new_number):
                suma +=1
                repeat_check *= new_number
    print(suma)

a = int(input())
b = int(input())
zad(a,b)