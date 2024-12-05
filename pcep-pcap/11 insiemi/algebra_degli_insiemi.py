base_ottale = set([0, 1, 2, 3, 4, 5, 6, 7])
base_esadecimale = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F'])

unione = base_ottale | base_esadecimale
print(unione)
#

intersezione = base_ottale & base_esadecimale
print(intersezione)
#

unione_esclusiva = base_ottale ^ base_esadecimale
print(unione_esclusiva)










