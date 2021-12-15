def collision(sq1, sq2):
    ax1, ax2, ay1, ay2 = sq1
    bx1, bx2, by1, by2 = sq2

    if bx2 < ax1 or bx1 > ax2 or ay1 > by2 or ay2 < by1 or (bx2 < ax2 and bx1 > ax1 and by1 > ay1 and by2 < ay2):
        return False

    return True

def area(sq):
    x1, x2, y1, y2 = sq
    return (x2 - x1) * (y2 - y1)

def check_for_collisions(square_list, index):
    for i in range(index-1):
        if square_list[i] == None:
            break
        if collision(square_list[i], square_list[index-1]):
            return True
    return False

def len_Of_Non_None(T):
    ile = 0
    for i in T:
        if i == None:
            break
        ile += 1
    return ile

def rek(T, used, total_area=0, last=0, index=0):

    if check_for_collisions(used,index) or total_area > 2012:
        return False
    # print(len_Of_Non_None(used))
    if len_Of_Non_None(used) == 13:
        print(total_area)
        if total_area == 1012:
            return True
        return False

    for i in range(last, len(T)):
        sq = T[i]
        used[index] = sq
        if rek(T, used, total_area + area(sq), i, index+1):
            return True
    # print(total_area)
    return False

T = [
    (20, 40, 0, 10),
    (10, 20, 10, 20),
    (1000, 1002, 1000, 1002),
    (1003, 1005, 1003, 1005),
    (1006, 1008, 1006, 1008),
    (55, 65, 55, 65),
    (66, 76, 66, 76),
    (77, 87, 77, 87),
    (88, 98, 88, 98),
    (0, 10, 0, 10),
    (11, 21, 11, 21),
    (22, 32, 22, 32),
    (33, 43, 33, 43),
    (44, 54, 44, 54),
    (120, 130, 120, 130),

]
used = [None for i in range(13)]

print(rek(T, used))