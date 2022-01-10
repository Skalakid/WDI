# 2. Zastosowanie listy odsyłaczowej do implementacji
# tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.
class Node:
    def __init__(self, index, x):
        self.index = index
        self.val = x
        self.next = None


class SparseArr:
    def __init__(self):
        self.first = None

    def set_val(self, index, val):
        elem = Node(index, val)
        if self.first == None: # 0 elementów
            self.first = elem
            return

        if index < self.first.index: # index mniejszy niż first.index
            elem.next = self.first
            self.first = elem
        else:

            curr = self.first
            prev = self.first
            while curr.next is not None:
                if index == curr.index:
                    return
                if index < curr.index:
                    break
                prev = curr
                curr = curr.next
            if index < curr.index:
                elem.next = curr
                prev.next = elem
                return
            if index != curr.index: curr.next = elem

    def get_val(self, index):
        curr = self.first
        while curr is not None:
            if index == curr.index:
                return curr.val
            curr = curr.next
        return -1

    def print_list(self):
        curr = self.first
        while curr is not None:
            print(" -> " + str(curr.index) + ": " + str(curr.val), end="")
            curr = curr.next
        print()

set = SparseArr()
set.set_val(2, 10)
set.set_val(4, 240)
set.set_val(1, 1)
set.set_val(3, 20)
set.print_list()
print(set.get_val(1))
print(set.get_val(2))
print(set.get_val(3))
print(set.get_val(4))