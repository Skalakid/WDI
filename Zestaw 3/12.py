t = [1,2,3,2,4,6,8]
r = t[1] - t[0]
dl = 2
max_dl_plus = 0
max_dl_minus = 0
isFirst = True
for i in range(1,len(t)):
    if r == t[i] - t[i-1]:
        dl += 1
    else:
        if r > 0 and max_dl_plus < dl:
            max_dl_plus = dl

        if r < 0 and max_dl_minus < dl:
            max_dl_minus = dl
        dl = 2
        r = t[i] - t[i-1]
print(max_dl_plus, max_dl_minus)