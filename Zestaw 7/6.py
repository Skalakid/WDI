class Node:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def push_back(head, val):
    while head.next is not None: # znajduje ostatni element który nie wskazuje na żadnego nexta
        head = head.next

    head.next = Node(val) # wstawienie nowego Node na koniec

def print_node(first):
    while first is not None:
        print(first.val)
        first = first.next

first = Node(10)
push_back(first, 12)
print_node(first)