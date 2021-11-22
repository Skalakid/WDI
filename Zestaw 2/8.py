def get_next_unsumable_num(n):
    n += 1
    while True:
        f1, f2 = 1, 0
        f_suma = 0
        while f_suma < n:
            f_suma += f1
            f1, f2 = f1+f2, f1

        f1, f2 = 1, 0
        while f_suma > n:
            f_suma -= f1
            f1, f2 = f1+f2, f1

        if f_suma != n:
            return n
        n += 1

n = int(input())
print(get_next_unsumable_num(n))
