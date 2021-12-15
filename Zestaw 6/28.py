def num_of_ones(n):
    ile = 0
    copy_n = n
    while copy_n != 1:
        if copy_n % 2 == 1:
            ile += 1
        copy_n //= 2

    return ile+1

def rek(T, i=0, l1=0, l2=0, l3=0):
    if i == len(T):
        return l1 == l2 == l3

    ones = num_of_ones(T[i])
    return rek(T, i+1, l1+ones, l2, l3) or rek(T, i+1, l1, l2+ones, l3) or rek(T, i+1, l1, l2, l3+ones)


T =  [5, 7, 15]
print(rek(T))