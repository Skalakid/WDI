def rek(T, i=0, kroki=0):
    # print(T, i, kroki)
    if i == len(T)-1:
        return kroki
    if i >= len(T):
        return -1

    dzielnik = 2
    flag = -1
    while T[i] != 1 and dzielnik < T[i]:
        if T[i] % dzielnik == 0:
            if i+dzielnik < len(T):
                flag = rek(T, i+dzielnik, kroki+1)
            while T[i] % dzielnik == 0:
                T[i] //= dzielnik
        dzielnik += 1

    return flag

T = [6,0,2,15,1,1,2,1,1]
print(rek(T))