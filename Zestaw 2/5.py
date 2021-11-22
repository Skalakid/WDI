import math

def getDigit(n, index):
    return n//(10**index)%10

n = int(input())
len_n = int(math.log10(n))+1
suma = 0
for mask in range(1, 2**len_n):
    result = 0
    iter = 0
    for i in range(len_n):
        if (1 << i) & mask:
            result += getDigit(n, i) * 10 ** iter
            iter +=1
    if result != 0 and result % 7 == 0:
        suma += 1
        print(result)

print(suma)