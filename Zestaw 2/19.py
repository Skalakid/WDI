a = int(input())
b = int(input())

tab = [None for i in range(1000)]
print(a//b, end=".")
found = False
a = a%b
x = 0
while a != 0 and x < 1000:
    a *= 10
    tab[x] = a

    for i in range(x):
        if tab[i] == tab[x]:
            found = True
            break
    if found:
        break

    a = a%b
    x += 1

if a==0 and x == 1000:
    for i in range(x):
        print(tab[i]//b, end="")
else:
    i = 0
    # wypisanie przed okresem
    while tab[i] != tab[x]:
        print(tab[i]//b, end="")
        i+=1

    if i < x:
        print("(", end="")
        while i != x:
            print(tab[i]//b, end="")
            i+=1
        print(")", end="")
