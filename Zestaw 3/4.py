def silnia(n):
    if n == 0:
        return 1
    else:
        return silnia(n-1)*n

n = int(input())+1

e = [0 for _ in range(n)]
e[0] = 1

for i in range (1, n+1):
    sln = silnia(i)
    reszta=1
    for d in range(n):
        e[d] += reszta//sln
        # reszta -=((reszta//sln)*sln)
        # reszta*=10
        reszta = (reszta%sln)*10
    print(e)

for i in range(n-1, 0, -1):
    if e[i] > 9:
        e[i-1] += (e[i] //10)
        e[i] %= 10

print(e[0], end=".")
for i in range(1, n):
    print(e[i], end="")