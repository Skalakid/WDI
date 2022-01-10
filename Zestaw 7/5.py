class Node:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def push_back(val, zb):
    if zb == None:
        return Node(val)
    if zb.next == None and zb.val == None:
        zb.val = val
        return
    while zb.next is not None:
        zb = zb.next
    zb.next = Node(val)

def printSet(zb):
    curr = zb
    while curr is not None:
        print(" ->", curr.val, end="")
        curr = curr.next
    print()


zb1 = Node(1)
push_back(33, zb1)
push_back(22, zb1)
push_back(12, zb1)
push_back(3, zb1)
push_back(5, zb1)
push_back(2, zb1)
printSet(zb1)

def sort(zb):
    z0 = Node()
    z1 = Node()
    z2 = Node()
    z3 = Node()
    z4 = Node()
    z5 = Node()
    z6 = Node()
    z7 = Node()
    z8 = Node()
    z9 = Node()

    while zb is not None:
        if zb.val % 10 == 0:
            push_back(zb.val, z0)
        elif zb.val % 10 == 1:
            push_back(zb.val, z1)
        elif zb.val % 10 == 2:
            push_back(zb.val, z2)
        elif zb.val % 10 == 3:
            push_back(zb.val, z3)
        elif zb.val % 10 == 4:
            push_back(zb.val, z4)
        elif zb.val % 10 == 5:
            push_back(zb.val, z5)
        elif zb.val % 10 == 6:
            push_back(zb.val, z6)
        elif zb.val % 10 == 7:
            push_back(zb.val, z7)
        elif zb.val % 10 == 8:
            push_back(zb.val, z8)
        else:
            push_back(zb.val, z9)

        zb = zb.next

    ans = Node()

    while z0 is not None:
        push_back(z0.val, ans)
        z0 = z0.next

    while z1 is not None:
        push_back(z1.val, ans)
        z1 = z1.next

    while z2 is not None:
        push_back(z2.val, ans)
        z2 = z2.next

    while z3 is not None:
        push_back(z3.val, ans)
        z3 = z3.next

    while z4 is not None:
        push_back(z4.val, ans)
        z4 = z4.next

    while z5 is not None:
        push_back(z5.val, ans)
        z5 = z5.next

    while z6 is not None:
        push_back(z6.val, ans)
        z6 = z6.next

    while z7 is not None:
        push_back(z7.val, ans)
        z7 = z7.next

    while z8 is not None:
        push_back(z8.val, ans)
        z8 = z8.next

    while z9 is not None:
        push_back(z9.val, ans)
        z9 = z9.next

    return ans

printSet(sort(zb1))



