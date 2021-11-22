def zad(n):
    last_digit = n%10
    n //= 10
    while n > 0:
        if n%10 >= last_digit:
            return False
        n //= 10
    return True


n = int(input())
print(zad(n))