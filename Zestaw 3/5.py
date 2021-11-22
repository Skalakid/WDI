t = [0 for i in range(10)]
index = 0
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(10):
        if n > t[i]:
            t[i], n = n, t[i]
print(t[-1])
