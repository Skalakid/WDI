class Node:
    def __init__(self, x, nex = None):
        self.val = x
        self.next = None

def push_back(head, val):
    while head.next is not None:
        head = head.next

    head.next = Node(val)

def remove_last(head):
    curr = head
    prev = None
    while curr.next is not None:
        prev = curr
        curr = curr.next

    prev.next = None # usuwamy połączenie z ostatnim elementem

def print_node(first):
    while first is not None:
        print("->" + str(first.val), end="")
        first = first.next
    print()

first = Node(10)
push_back(first, 11)
push_back(first, 12)
push_back(first, 13)

print_node(first)

remove_last(first)

print_node(first)



