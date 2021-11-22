def isFib(n):
    fib1, fib2 = 1, 1
    while fib1 <= n:
        if fib1 == n:
            return True
        fib1, fib2 = fib1+fib2,fib1
    return False

n = int(input())
f1, f2 = 1, 1
while f1 <= (n//2)+1:
    if n % f1 == 0 and isFib(n//f1):
        print(True)
        break
    f1,f2=f1+f2,f1
else:
    print(False)