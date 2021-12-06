import math


def rek(t, index, sum_el=0, sum_in=0, length=0, best_len=math.inf):
    if index >= len(t):
        return sum_el == sum_in and sum_el > 0, sum_el, length

    best_s = 0
    poss = False

    ans, s, l = rek(t, index+1, sum_el, sum_in, length, best_len)
    if ans and l < best_len:
        best_s = s
        best_len = l
        poss = True

    ans, s, l = rek(t, index + 1, sum_el + t[index], sum_in + index, length + 1, best_len)
    if ans and l < best_len:
        best_s = s
        best_len = l
        poss = True

    return poss, best_s, best_len

t = [1,7,3,5,11,2]
print(rek(t, 0))