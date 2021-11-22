def zad(T):
    sum_index = 0
    sum_el = T[0]
    dl = 0
    if sum_index == sum_el:
        dl = 1
    max_dl = 0
    for i in range(1,len(T)):
        sum_el += T[i]
        sum_index += i
        if T[i - 1] < T[i] and sum_el == sum_index:
            dl += 1
        else:
            if max_dl < dl:
                max_dl = dl
            dl = 1
            sum_index = i
            sum_el = T[i]

    if max_dl < dl:
        max_dl = dl
    return max_dl


T = [0, 1, 2, 2, 8, 5, 4, 7, 8]
print(zad(T))