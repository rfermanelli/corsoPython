l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l2 = l1[len(l1)//2:]
print(l2)

l2[3] = 'g'
print(l2)

l2[1:3] = [0]
print(l2)

l2[len(l2):] = ['ciao', (0, 1)]
print(l2)

l2[:0] = [-2, -1]
print(l2)

l2[len(l2):] = [[0, 1]]
print(l2)
print((l2[len(l2) - 1][0]))

l3 = [('i', 4)]
l1.append(l3)
print(l1)

l4 = ['x', 'y', 'z']
l2.extend(l4)
print(l2)

l4.insert(2, 'w')
print(l4)

l4.insert(-2, 'j')
print(l4)

del(l4[2])
print(l4)

l5 = [0, 1, 2, 3]
print(l5)
del(l5)
#print(l5)

l6 = [0, 1, 2, 2, 2, 3, 3, 5]
l6.remove(2)
print(l6)
l6.remove(3)
print(l6)

if 7 in l6:
    l6.remove(7)

l6.reverse()
print(l6)

# Spostare gli ultimi tre elementi dalla fine all’inizio conservandone l’ordine
l6[:0] = l6[len(l6) - 3:]
del(l6[len(l6) - 3:])
print(l6)

l7 = [0, 1, 5, 6, 2, 3]
print(l7)
l7.sort()
print(l7)

l7 = [9, 0, 4, 3, 1, 7, 6, 5, 8]
l8 = sorted(l7)
print(l7)
print(l8)

l9 = [[9, 4], [2, 5], [2, 3], [8, 5]]
l9.sort()
print(l9)

l10 = ['alfa', 'Iota', 'gamma', 'beta', 'Sigma', 'teta']


def f(word):
    return len(word)

l10.sort()
print(l10)

l10 = ['alfa', 'Iota', 'gamma', 'Beta', 'Sigma', 'teta']
l10.sort(key = f)
print(l10)

l11 = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]


def middle(lst):
    return lst[1]

l11.sort(key = middle)
print(l11)

l12 = l10 + l11
print(l12)

print(min(l10))
print(max(l10))
print(l12.index([4, 0, 1]))
print(l12.count('alfa'))

def eraseEl(lst, el):
    if el in lst:
        lst.remove(el)
    else:
        print(el, 'non è in:', lst)


eraseEl(l10, 'ciao')

def eraseElc(lst, el):
    if lst.count(el) > 1:
        lst.remove(el)
    elif lst.count(el) == 1:
        print(el, 'è in :', lst, 'solo una volta')


eraseElc(l10, 'ciao')

m1 = [[[0, 0, 0], [1, 1, 1], [2, 2, 2]], [[3, 3, 3,], [4, 4, 4,], [5, 5, 5]], [[6, 6, 6], [7, 7, 7], [8, 8, 8]]]
print(m1[2][1][0])

import copy
m2 = copy.deepcopy(m1)
print(m2)



