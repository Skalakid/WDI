class Node():
    def __init__(self, x):
        self.val = x
        self.next = None

class Set():
    def __init__(self):
        self.first = None

def member(val , zb):
        if zb.first != None:
            curr = zb.first
            while curr is not None:
                if curr.val == val:
                    return True
                curr = curr.next
        return False

def insert(val, zb):
    if zb.first == None: # przypadek gdy zbiór jrest pusty i checmy dodać 1 element
        zb.first = Node(val)
    else:
        if not member(val, zb):
            new = Node(val)
            if val < zb.first.val: # przypadek gdy nowy element jest mniejszy od pierwszego w zbiorze. Chcemy by ten nowy był teraz first
                new.next = zb.first
                zb.first = new
            else: # przypadek gdy val jest większy niż pierwszy element
                curr = zb.first
                prev = zb.first
                while curr is not None: # szukamy miejsca gdzie val jest mniejsdzy od jakiejś wartości w zbiorze
                    if val < curr.val:
                        break # gdy znajdziemy to miejsce break i dodajemy ;)
                    prev = curr
                    curr = curr.next

                prev.next = new
                new.next = curr

def delete(val, zb):
    if zb.first != None:
        if zb.first.next == None: # przypadek gdy jest tylko jeden element w zbiorze
            zb.first = None
        else:
            curr = zb.first
            prev = zb.first
            while curr is not None:
                if curr.val == val:
                    prev.next = curr.next
                    break
                prev = curr
                curr = curr.next

def printSet(zb):
    curr = zb.first
    while curr is not None:
        print(" ->", curr.val, end="")
        curr = curr.next
    print()



myset = Set()
insert(2, myset)
insert(2, myset)
insert(4, myset)
insert(32, myset)
insert(1, myset)
delete(32, myset)
printSet(myset)


