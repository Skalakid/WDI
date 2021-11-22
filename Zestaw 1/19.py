element = 1
i = 1
e = 0
silnia = 1
while element != 0:
    element = 1/ silnia
    silnia *= i
    i+=1
    e += element
print(e)