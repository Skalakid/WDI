# 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
# struktury listy odsyłaczowej.
# - czy element należy do zbioru
# - wstawienie elementu do zbioru
# - usunięcie elementu ze zbioru

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Set:
    def __init__(self):
        self.first = None

    def contains(self, val):
        if self.first != None:
            curr = self.first
            while curr is not None:
                if curr.val == val:
                    return True
                curr = curr.next
        return False

    def add(self, val):
        new = Node(val)
        if self.first == None: # gdy lista jest pusta
            self.first = new
        elif not self.contains(val):
            if self.first.val > val: # gdy element jest miejszy od pierwszego w liście
                new.next = self.first
                self.first = new
            else:
                curr = self.first
                prev = self.first
                while curr.next is not None:
                    if curr.val > val: # dodawanie elementu do środka
                        break
                    prev = curr
                    curr = curr.next

                if curr.val > val: # dodawanie jako przed ostatni element
                    new.next = curr
                    prev.next = new
                else:
                    curr.next = new # dodawanie jako ostatni element

    def remove(self, val):
        if self.first != None:
            if self.first.val == val:
                self.first = self.first.next
            else:
                curr = self.first
                prev = self.first
                while curr is not None:
                    if curr.val == val:
                        prev.next = curr.next
                        return
                    prev = curr
                    curr = curr.next


    def print(self):
        curr = self.first
        while curr is not None:
            print("->" + str(curr.val), end="")
            curr = curr.next
        print()


set = Set()
set.add(10)
set.add(9)
set.add(13)
set.add(12)
set.add(12)
set.add(11)
set.remove(9)
set.remove(13)
set.print()

