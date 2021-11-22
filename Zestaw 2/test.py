import math


def convert_to_bin(n):
    result = 0
    pow = 0
    while n > 0:
        if n % 2 == 1:
            result += 10**pow
        n //= 2
        pow+=1
    return result

def num_of_ones(n):
    suma = 0
    while n > 0:
        if n%10 == 1:
            suma += 1
        n //= 10
    return suma

def length(n):
    return int(math.log10(n))+1

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def zad(a, b):
    len_a = int(math.log10(a)) + 1
    len_b = int(math.log10(b)) + 1
    len_c = len_b + len_a
    repeat_check = 1
    suma = 0
    for i in range(2 ** (len_c), 2 ** (len_c + 1)):
        mask = convert_to_bin(i)

        if num_of_ones(mask)-1 != length(b):
            continue

        print(mask)
        new_number = 0
        copy_a = a
        copy_b = b
        pow = 0
        while mask > 1:
            if mask % 10 == 0:
                new_number += (copy_a % 10) * 10 ** pow
                copy_a //= 10
            else:
                new_number += (copy_b % 10) * 10 ** pow
                copy_b //= 10

            pow += 1
            mask //= 10

        if repeat_check % new_number != 0:
            if isPrime(new_number):
                suma += 1
                repeat_check *= new_number

    print(suma)

a = int(input())
b = int(input())
zad(a,b)

