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

def reverse(zb, ans):
    if zb.next != None:
        reverse(zb.next, ans)
    if zb.val != None:
        push_back(zb.val, ans)

zb1 = Node(1)
push_back(2, zb1)
push_back(2, zb1)
push_back(3, zb1)
printSet(zb1)
ans = Node()
reverse(zb1, ans)
printSet(ans)