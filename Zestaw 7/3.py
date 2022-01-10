#3. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.

# ROZWIĄZANIE NA DOLE
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Set:
    def __init__(self):
        self.first = None

    def add(self, val):
        if self.first == None:  # przypadek gdy zbiór jrest pusty i checmy dodać 1 element
            self.first = Node(val)
        else:
            new = Node(val)
            if val < self.first.val:  # przypadek gdy nowy element jest mniejszy od pierwszego w zbiorze. Chcemy by ten nowy był teraz first
                new.next = self.first
                self.first = new
            else:  # przypadek gdy val jest większy niż pierwszy element
                curr = self.first
                prev = self.first
                while curr is not None:  # szukamy miejsca gdzie val jest mniejsdzy od jakiejś wartości w zbiorze
                    if val <= curr.val:
                        break  # gdy znajdziemy to miejsce break i dodajemy ;)
                    prev = curr
                    curr = curr.next

                prev.next = new
                new.next = curr

    def print(self):
        curr = self.first
        while curr is not None:
            print(" -> " + str(curr.val), end="")
            curr = curr.next
        print()

set1 = Set()
set1.add(1)
set1.add(2)
set1.add(25)
set1.add(432)
set1.print()

set2 = Set()
set2.add(3)
set2.add(4)
set2.add(4)
set2.add(43)
set2.add(4243)
set2.print()

# TU SIĘ ZACZYNA ZADANIE !!!
# iter
def merge_iter(zb1, zb2):
    new_set = Set()
    curr1 = zb1.first
    curr2 = zb2.first
    while curr1 is not None or curr2 is not None:
        if curr1 == None or curr1.val >= curr2.val:
            new_set.add(curr2.val)
            curr2 = curr2.next
        elif curr2 == None or curr1.val < curr2.val:
            new_set.add(curr1.val)
            curr1 = curr1.next

    new_set.print()
    return new_set

# rekurencja :-D
def merge_rek(zb1, zb2):
    def rek(l1, l2, ans):
        if l1 == None and l2 == None:
         return ans

        if l1 != None and l2 != None:
            if l1.val < l2.val:
                ans.add(l1.val)
                return rek(l1.next, l2, ans)
        else:
            ans.add(l2.val)
            return rek(l1, l2.next, ans)

        if l1 == None:
            ans.add(l2.val)
            return rek(l1, l2.next, ans)
        else:
            ans.add(l1.val)
            return rek(l1.next, l2, ans)



    ans = Set()
    return rek(zb1.first, zb2.first, ans)


merge_iter(set1, set2)
merge_rek(set1, set2).print()

