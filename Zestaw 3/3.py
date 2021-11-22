import math

n = int(input())
numbers = []

for i in range(2,n):
    numbers.append(i)

print(numbers)

for i in range(2,int(math.sqrt(n))+1):
    wielokrotnosc = i*2
    while wielokrotnosc < n:
        if wielokrotnosc in numbers:
            numbers.remove(wielokrotnosc)
        wielokrotnosc += i
print(numbers)