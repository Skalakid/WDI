def zad8(T):
    start_x = 0
    start_y = len(T)-2
    max_dl = 0
    while start_x < len(T)-2:
        x = start_x + 2
        y = start_y + 2
        q = T[start_y+1][start_x+1] / T[start_y][start_x]
        dl = 2


        while 0<=x<len(T) and 0<=y<len(T):
            if q == T[y][x] / T[y-1][x-1]:
                dl += 1
            else:
                if max_dl < dl:
                    max_dl = dl
                dl = 2
                q = T[y][x] / T[y-1][x-1]
            x+=1
            y+=1
        if max_dl < dl:
            max_dl = dl




        if start_y == 0:
            start_x += 1
        else:
            start_y -= 1

    return max_dl


T = [
    [1,1,1,1],
    [2,2,2,2],
    [4,4,4,4],
    [8,8,8,8]
]
print(zad8(T))