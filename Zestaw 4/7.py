# Funkcja sprawdza w którym wierszu znajduje się kolejny element n. Wszystko oparte jest o tablice T3 która wyznacza element w danym wierszu.
def spr_czy_el_w_innym_wierszu_T1(n):
    for i in range(N):
        if T3[i] < N and T1[i][T3[i]] == n:
            return i
    return -1

def zad():
    T2_el = 0

    while T2_el < N**2:
        print(1)
        #szukanie najmniejszego elementu po wierszach, gdzie indeks w wierszu jest zależny od tabelki T3
        max_el = -1
        max_el_i = 0
        for i in range(N):
            if T3[i] > -1:
                spr_el = T1[i][T3[i]]
                if spr_el > max_el:
                    max_el = spr_el
                    max_el_i = i

        T3[max_el_i] -= 1
        T2[T2_el] = max_el
        T2_el += 1
    print(T2)

N = 4
T1 = [
    [1,2,3,4],
    [4,5,5,9],
    [3,5,8,9],
    [6,6,7,7]
]
T2 = [0 for _ in range(N*N)]
T3 = [N-1 for _ in range(N)]
zad()

