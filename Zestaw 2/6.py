n = int(input())
min_r = 100000
el = []
for i in range(2, n//2+1):
    if n % i == 0:
        if min_r > abs(i - (n//i)):
            min_r = abs(i - (n//i))
            el = [i, n//i]

print(el)