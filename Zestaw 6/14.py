def hanoi(n, A, B, C, i=0):  # przeniesienie wszystkich z A na C z wykorzystniem B
    if n > 0:
        hanoi(n-1, A, C, B, i+1) # przeniesienie z A na B z wykorzystaniem C
        C[i] = A[i] # najwięszy który został na A idzie na C
        A[i] = 0
        hanoi(n-1, B, A, C, i+1) # przeniesienie z B na C z wykorzystaniem A


A = [1, 2, 3, 4]
B = [0]*len(A)
C = [0]*len(A)
hanoi(4, A, B, C)
print(C)