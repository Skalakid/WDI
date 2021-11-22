s = str(input())
t = [None for _ in range(len(s)//2)]
index = 0
for i in range(1,(len(s)//2) + 1):
    if len(s)%i == 0:
        t[index] = i
        index +=1
t = t[:index]

czyWiel = False
for length in t:
    czyWiel = True
    for j in range(1, len(s)//length):
        for k in range(length):
            if s[k] != s[k + (length*j)]:
                czyWiel = False
                break
        if not czyWiel:
            break
    if czyWiel:
        break

if czyWiel:
    print("TAK")
else:
    print("NIE")