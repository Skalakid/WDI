def czyZgodne(n):
    ile = 0
    while n >0:
        if n % 2 == 1:
           ile += 1
        n//=2
    return ile

def spr(T1, T2):
    y = 0
    x = 0
    while y + len(T1) < len(T2):
        while x + len(T1) < len(T2):

            ile = 0
            for i in range(len(T1)):
                for j in range(len(T1)):
                    if czyZgodne(T1[i][j]) == czyZgodne(T2[i][j]):
                        ile +=1
            if (ile/len(T1)**2)*100 > 33:
                return True
            x+=1
        y+=1
    return False



N1 = 2
N2 = 4
T1 = [[i+5 for _ in range(N1)]for i in range(N1)]
T2 = [[i+6 for _ in range(N2)]for i in range(N2)]

for i in range(N1):
    print(T1[i])
print()
for i in range(N2):
    print(T2[i])

print(spr(T1,T2))