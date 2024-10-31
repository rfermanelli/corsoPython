two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

#
# La classe Iterator simula il comportamento della funzione range()
class Iterator:
    def __init__(self, valore):
        self.__valore = valore
        self.__passo = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__passo += 1
        if self.__passo == self.__valore:
            raise StopIteration
        else:
            return self.__passo

# La funzione map() ha i due parametri: lambda, Iterator(10), il secondo parametro deve essere iterabile
for i in map(lambda x: x**2, Iterator(10)):
    print(i, end=' ')
print()

# La funzione filter() è equivalente alla funzionme map()
# La differenza riguarda gli elementi restituiti che sono filtrati dalla funzione al primo argomemto
# Se l'elemento iterato supera la condizione allora entra a far parte dell'iterabile
for i in filter(lambda x: x % 2 == 0, Iterator(10)):
    print(i, end=' ')


