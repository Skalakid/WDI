def odwaz(T, suma , is_taken, i=0):
    if suma == 0:
        return True
    if i == len(T):
        return False

    if odwaz(T, suma + T[i], is_taken, i+1):
        is_taken[i] += T[i]
        return True
    if odwaz(T, suma - T[i], is_taken, i+1):
        is_taken[i] -= T[i]
        return True
    if odwaz(T, suma , is_taken, i+1):
        return True
    return False

T = [1,2,3,4]
is_taken = [0 for _ in range(len(T))]
m = int(input())
print(odwaz(T, m, is_taken))
for i in range(len(T)):
    print(is_taken[i])