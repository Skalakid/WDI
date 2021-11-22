
s = str(input())
samogIndexes = [None for i in range(len(s))]
index = 0
n = 0
samog = ['a', 'e', 'i', 'o', 'u', 'y']
while n < len(s):
    if s[n] in samog:
        samogIndexes[index] = n
        index+=1
    n+=1
samogIndexes =samogIndexes[:index]

podzialy = []

ile = 1
for i in range(1, len(samogIndexes)):
     ile *= samogIndexes[i]-samogIndexes[i-1]
print(ile)
