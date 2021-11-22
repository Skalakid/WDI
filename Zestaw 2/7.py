def next_a(n):
    return n*n+n+1

num = int(input())
a = 1
i = 1
while a <= num:
    if num % a == 0:
        print(True)
        break
    a = next_a(i)
    i+= 1
else:
    print(False)