class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def __eq__(self, other):
        if isinstance(other, Persona):
            return self.nome == other.nome and self.eta == other.eta
        return False

persona_1 = Persona("Mario", 'Rossi', 30)
persona_2 = Persona("Mario", 'Rossi', 30)

print(persona_1 == persona_2)
print(persona_1.__eq__(persona_2))
print(persona_1 is persona_2)

