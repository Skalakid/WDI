import math


def next_a(a,b):
    return math.sqrt(a*b)

def next_b(a,b):
    return (a + b)/2.0

eps = 1/1000
a = int(input())
b = int(input())
while(abs(a-b) > eps):
    a,b = next_a(a,b), next_b(a,b)
print((a+b)/2)