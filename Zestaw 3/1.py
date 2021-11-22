from math import *

def change(n, sys):
    ozn = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    tab = []
    tnp = 0
    while n>0:
        tab.append(ozn[n%sys])
        n//=sys
    tab.reverse()
    print(tab)

n = int(input())
sys= int(input())
change(n, sys)
