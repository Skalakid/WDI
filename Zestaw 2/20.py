def check(a,b,base):
    copy1, copy2 = a, b
    while copy1 > 0:
        digit1 = copy1 % base
        copy1 //= base
        while copy2 > 0:
            digit2 = copy2 % base
            copy2 //= base

            if digit2 == digit1:
                return False
    return True

a = int(input())
b = int(input())
for i in range(2,17):
    if check(a, b, i):
        print(i)
        break