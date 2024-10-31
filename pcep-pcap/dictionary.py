d = {}
print(d)

d['one'] = 1
d['two'] = 2

print(list(d.keys()))
print(list(d.values()))

print(d.__hash__)
"""
nome1 = input('nome1: ')
età1 = input('età1: ')

nome2 = input('nome2: ')
età2 = input('età2: ')

nome3 = input('nome3: ')
età3 = input('età3: ')

d[nome1] = età1
d[nome2] = età2
d[nome3] = età3

nome = input('Qual è il nome di cui vuoi sapere l\'età? ')
print(d[nome])
"""

x = {'a':1, 'b':2, 'c':3, 'd':4}
y = {'a':6, 'e':5, 'f':6}
del x['d']
z = x.setdefault('g', 7)
x.update(y)
print(x)

k = ('red', 'richards')
print(k)
d2 = {}
d2[k] = 'mr fantastic'
print(d2)

# Le matrici sparse
matrix = [[3, 0, -2, 11], [0, 9, 0, 0], [0, 7, 0, 0], [0, 0, 0, -5]]
matrixS = {(0, 0): 3, (0, 2): -2, (0, 3): 11, (1, 1): 9, (2, 1): 7, (3, 3): -5}
rownum = input('numero di riga: ')
colnum = input('numero di colonna: ')
if (rownum, colnum) in matrixS:
    element = matrixS[rownum][colnum]
else:
    element = 0
print('l\'elemento di riga', rownum, 'e di colonna', colnum, 'è', element)