n = int(input())
s = n / 2
eps = 1/1000
while abs(n/(s*s)- s) > eps:
    s = (s + (n/(s*s)))/2
print(s)