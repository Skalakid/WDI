def zad():
    min_el = 1000000
    min_count = 0
    max_el = 0
    max_count = 0
    for i in range(len(T)):
        if T[i] > max_el:
            max_el = T[i]
        if T[i] < min_el:
            min_el = T[i]

    for i in range(len(T)):
        if T[i] == max_el:
            max_count += 1
        if T[i] == min_el:
            min_count += 1

    if min_count == 1 and max_count == 1:
        return True
    return False

T = [0, 1, 2, 3, 4, 5 ,4, 54,5456,3345,1,3, 2,3 ,2]
print(zad())