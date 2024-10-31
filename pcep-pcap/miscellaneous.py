# L'istanza di classe come iteratore
import random


class Generatore:
    def __init__(self, v):
        self.passo = v
        self.contatore = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.contatore < self.passo:
            self.contatore += 1
            return random.randint(1, 20)
        else:
            raise StopIteration


for i in Generatore(5):
    print(i, end=' ')

# La list comprehension come iteratore con le funzioni map() e filter()
print()
lista_generatore = (map(lambda x:  x ** 2, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)))
lista_filtrata = (filter(lambda y: y % 2 == 0, [7, 5, 4, 3, 8, 9, 0]))

for i in lista_generatore:
    print(i, end=' ')

print()
for i in lista_filtrata:
    print(i, end=' ')

# La list comprehension con una espressione condizionale
print()
l = [x / 2 if x % 2 == 0 else x for x in range(20)]

print(l)

# Date
import datetime

d_1 = datetime.time
print(d_1)






