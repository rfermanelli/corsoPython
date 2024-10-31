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
class Impiegato(Persona):
    def __init__(self, contratto, matricola, settore, ruolo):
        Persona.__init__(self, 'Roberto', 'Rossi', 40)
        self.contratto = contratto
        self.matricola = matricola
        self.settore = settore
        self.ruolo = ruolo

roberto = Impiegato('Indeterminato', '00100', 'IT', 'Programmatore')
print(roberto.nome)
print(roberto.cognome)
print(roberto._Persona__eta)
print(roberto.matricola)
print(roberto.settore)
print(roberto.ruolo)






