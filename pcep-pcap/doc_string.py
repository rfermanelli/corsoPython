def fattoriale(n):
    '''Calcolo del fattoriale di n.'''
    r = 1
    while n > 0:
        r = r * n
        n = n - 1
    return r

print(fattoriale(10))

fattoriale_commento = fattoriale.__doc__
print(fattoriale_commento)
