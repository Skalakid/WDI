def next_a(a):
    return (a%2)*(3*a+1)+(1-a%2)*a/2


max_steps=0
for i in range(2,10000):
    steps = 0
    wyraz = i

    while wyraz != 1:
        wyraz = next_a(wyraz)
        steps +=1

    if max_steps < steps:
        max_steps = steps

print(max_steps)