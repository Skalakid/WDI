# Funkcja sprawdza w którym wierszu znajduje się kolejny element n. Wszystko oparte jest o tablice T3 która wyznacza element w danym wierszu.
def spr_czy_el_w_innym_wierszu_T1(n):
    for i in range(N):
        if T3[i] < N and T1[i][T3[i]] == n:
            return i
    return -1

def zad():
    index = 0
    T2_el = 0

    while index < N**2:
        #szukanie najmniejszego elementu po wierszach, gdzie indeks w wierszu jest zależny od tabelki T3
        min_el = 1000000
        min_el_i = 0
        for i in range(N):
            if T3[i] < N:
                spr_el = T1[i][T3[i]]
                if spr_el < min_el:
                    min_el = spr_el
                    min_el_i = i

        # Gdy znajdzie najmniejszy element to do T3 w odpowiednim indeksie (oznaczającym numer wiersza T1) dodawane jest 1
        # Oznacza to że ten element z T1 z wiersza 'min_el_i' już wykożystaliśmy i patrzymy na następny po nim
        T3[min_el_i] += 1

        # Jeżeli nie ma kolejnego elementu o tej wartości to wpisz element do T[T2_el]
        if spr_czy_el_w_innym_wierszu_T1(min_el) == (-1):
            print(min_el, min_el_i, "!!")
            T2[T2_el] = min_el
            T2_el += 1
        else: # jeśeli jest, to dopóki nie znajdzie wszystkich elementów o tej samej wartości wzdłuż i wszerz odpowiednio przesówa indeksy T3 (dodaje jedynki)
            print(min_el, min_el_i)
            nextEl = spr_czy_el_w_innym_wierszu_T1(min_el)
            while nextEl > -1:
                print(min_el, nextEl)
                T3[nextEl] += 1
                index += 1
                nextEl = spr_czy_el_w_innym_wierszu_T1(min_el)
        index+=1
    print(T2)

N = 4
T1 = [
    [1,2,3,4],
    [4,5,5,9],
    [3,5,8,9],
    [6,6,7,7]
]
T2 = [0 for _ in range(N*N)]
T3 = [0 for _ in range(N)]
zad()

