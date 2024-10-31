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


for i in Iterator(10):
    print(i)

