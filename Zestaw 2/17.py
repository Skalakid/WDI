import math

def f(x):
    return x**x - 2020

def f_1(x):
    return (x**x)*(math.log(x)+1)

eps = 1/1000
x0 = 5
while abs(x0 - (f(x0)/f_1(x0))) > eps:
    x0-=1
