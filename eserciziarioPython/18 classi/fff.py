class Data:
    def __init__(self, giorno, mese, anno):
        self.giorno = giorno
        self.mese = mese
        self.anno = anno

    def __le__(self, other):
        if isinstance(other, Data):
            return (self.anno, self.mese, self.giorno) <= (other.anno, other.mese, other.giorno)
        return NotImplemented

data_1 = Data(15, 3, 2022)
data_2 = Data(16, 3, 2022)
data_3 = Data(15, 3, 2022)

print(d1 <= d2)  # True
print(d1 <= d3)  # True
print(d2 <= d1)  # False

