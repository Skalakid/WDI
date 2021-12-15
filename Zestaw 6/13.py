def rek(n, last, prnt=""):
    if n == 0:
        print(prnt)
    else:
        for i in range(last, n+1):
            rek(n-i, i, str(i)+'\t'+prnt)

rek(4,1)