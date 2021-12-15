def odwazniki(T, suma):
    if suma == 0:
        return True
    if not T:
        return False
    else:
        return odwazniki(T[1:], suma+T[0]) or odwazniki(T[1:], suma-T[0]) or odwazniki(T[1:], suma)

T = [1,3,5]
print(odwazniki(T, 7))