# y = 1/x

n = 100
xp = 1
xk = int(input())
dx = (xk - xp)/n
suma_f = 0
xi = 0
for i in range(1,n):
    xi = xp + (i/n)*(xk-xp)
    suma_f += 1/xi
print(dx*suma_f)
