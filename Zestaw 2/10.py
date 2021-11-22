def next_a(n):
    return 3*a + 1

n = int(input())
a=2
while a <= n:
    if n %a == 0:
        print(True)
        break
    a = next_a(a)
else:
    print(False)