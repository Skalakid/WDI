def uniqueDigits(n):
    tab = []
    while n > 0:
        digit = n%10
        isDigit = False
        if not digit in tab:
            tab.append(digit)
        n//=10
    tab.sort()
    return tab

a = int(input())
b = int(input())
if (uniqueDigits(a) == uniqueDigits(b)):
    print("TAK")
else:
    print("NIE")