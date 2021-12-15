def rek(T, expected, i=0, r1=0, r2=0, r3=0, counter=0):
    if counter == 3:
        # liczymy rezystancje
        res = 0
        res += r1
        if res != 0:
            res = (res * r2) / (res + r2)
        else:
            res += r2

        if res != 0:
            res = (res * r3) / (res + r3)
        else:
            res += r3

        res //= 1
        if res == expected:
            return True
        return False

    if i == len(T):
        return False

    return rek(T, expected, i+1, r1, r2, r3, counter) or rek(T, expected, i+1, r1+T[i], r2, r3, counter+1) \
           or rek(T, expected, i+1, r1, r2+T[i], r3, counter+1) or rek(T, expected, i+1, r1, r2, r3+T[i], counter+1)



T = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 130]
print(rek(T, 20))