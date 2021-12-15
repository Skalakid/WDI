
def szukajPodciagu(T):

    dl_pion = 0
    dl_poz = 0
    sum_pion = 0
    sum_poz = 0
    max_sum = 0


    for i in range(len(T)):
        for j in range(len(T)):

            k = j
            while k < len(T) :
                if dl_poz < 10:
                    sum_poz += T[i][k]
                    dl_poz += 1

                if dl_pion < 10:
                    sum_pion += T[k][i]
                    dl_pion += 1

                k += 1

            if max_sum < sum_poz:
                max_sum = sum_poz

            if max_sum < sum_pion:
                max_sum = sum_pion

            dl_pion = 0
            dl_poz = 0
            sum_pion = 0
            sum_poz = 0

    return max_sum
N = 12
T = [[_//(i+1) for _ in range(N)] for i in range(N)]
for i in range(N):
    print(T[i])

print(szukajPodciagu(T))

