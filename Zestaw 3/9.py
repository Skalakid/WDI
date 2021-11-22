n = int(input())
tab = [0 for _ in range(n)]
for i in range(n):
    tab[i] = int(input())
print('---')

maxDl = 0
dl = 0
for i in range(1, n):
    if tab[i-1] < tab[i]:
        dl+=1
    else:
        dl = 0
    if dl+1 > maxDl:
        maxDl = dl+1


print(maxDl)