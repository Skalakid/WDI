def odwaz(T, suma , i=0):
    if suma == 0:
        return True
    if i == len(T):
        return False
    else:
        return odwaz(T, suma + T[i], i+1) or odwaz(T, suma - T[i], i+1) or odwaz(T, suma , i+1)

T = [1,2,3,4]
m = int(input())
print(odwaz(T,m))