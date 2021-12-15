def solve(n):
    def getPodzielniki(n):
        dzielnik = 2
        T = [None for i in range(20)]
        i = 0
        while n != 1 and i < 20:
            if n % dzielnik == 0:
                T[i] = dzielnik
                i += 1
                while n % dzielnik == 0:
                    n //= dzielnik
            dzielnik += 1

        print(T)
        return T

    def rek(T, i=0, il=1):

        if i == len(T):
            if il == 1:
                return 0
            return il

        suma = 0
        suma += rek(T, i + 1, il)
        if T[i] != None:
            suma += rek(T, i + 1, il * T[i])

        return suma


    return rek(getPodzielniki(n))

print(solve(60))
