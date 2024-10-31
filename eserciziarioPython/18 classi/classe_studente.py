class Studente:
    def __init__(self, matricola, corso):
        self.matricola = matricola
        self.corso = corso
    def __repr__(self):
        return f"Studente(matricola = '{self.matricola}', corso = '{self.corso}')"
    def saluta(self):
        return f"Ciao, frequento il corso {self.corso}."

luigi = Studente(765, 'Lettere e filosofia')
mauro = Studente(367, 'Matematica')
elena = luigi
print(luigi is mauro)
print(elena is luigi)
print(luigi == mauro)
print(elena == luigi)


