def rek(T, suma, pom, index=0, new_suma=0):
    if new_suma == suma:
        return True

    if suma < new_suma or index == len(T):
        return False
    found = False
    for i in range(len(T)):
        if pom[i]:
            continue
        pc = pom[:]
        pc[i] = True
        found = found or rek(T,suma,pc,index+1,new_suma+T[index][i])
    return found




T = [
    [1,3],
    [7,7]
]
pom = [ False for i in range(len(T))]
print(rek(T, 10, pom))


