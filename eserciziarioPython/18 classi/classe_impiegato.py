import classe_persona
import classe_studente
class Impiegato(classe_studente.Studente, classe_persona.Persona):
    def __init__(self, contratto, matricola, settore, ruolo):
        classe_persona.Persona.__init__(self, 'Roberto', 'Rossi', 40)
        classe_studente.Studente.__init__(self, 346, 'Informatica')
        self.contratto = contratto
        self.matricola = matricola
        self.settore = settore
        self.ruolo = ruolo

roberto = Impiegato('Indeterminato', '00100', 'IT', 'Programmatore')

print(issubclass(Impiegato, classe_persona.Persona))




