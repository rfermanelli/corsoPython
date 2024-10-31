class Persona:
    __genere = 'Homo'
    __specie = 'Homo Sapiens'
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.__eta = eta
    def get_eta(self):
        return self.__eta
    def set_eta(self, nuova_eta):
        if nuova_eta > 0:
            self.__eta = nuova_eta
        else:
            raise ValueError("L'età deve essere un numero positivo.")
    def saluta(self):
        return f"Ciao, mi chiamo {self.nome}."