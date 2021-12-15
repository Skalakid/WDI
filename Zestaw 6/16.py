def sumaASCII(s):
    suma = 0
    for letter in s:
       suma += int(ord(letter))
    return suma

def ileSamoglosek(s):
    samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
    ile = 0
    for letter in s:
        if letter in samogloski:
            ile += 1
    return ile

def rek(s1, s2, index=0, str=""):
    if sumaASCII(s1) == sumaASCII(str) and ileSamoglosek(s1) == ileSamoglosek(str):
        print(str)
        return True

    if index == len(s2):
        return False

    return rek(s1, s2, index + 1, str) or rek(s1, s2, index + 1, str+s2[index])



print(rek('ulaaa', 'eddsffvaafsddxce'))