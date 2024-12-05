base_ottale = set([0, 1, 2, 3, 4, 5, 6, 7])
base_esadecimale = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F'])

differenza = base_esadecimale.difference(base_ottale)

intersezione = base_ottale.intersection(base_esadecimale)

print(differenza)
print(intersezione)



