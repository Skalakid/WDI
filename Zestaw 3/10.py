n = int(input())
tab = [0 for _ in range(n)]
for i in range(n):
    tab[i] = int(input())
print('---')

maxDl = 0
dl = 2
r = tab[1] - tab[0]
for i in range(2, n):
    if tab[i] - tab[i-1] == r:
        dl+=1
    else:
        dl = 2
        r = tab[i] - tab[i-1]
    if maxDl < dl:
        maxDl = dl
print(maxDl)