class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.__eta = eta  # Attributo privato

    def get_eta(self):
        return self.__eta

    def set_eta(self, nuova_eta):
        if nuova_eta > 0:
            self.__eta = nuova_eta
        else:
            raise ValueError("L'età deve essere un numero positivo.")


# Utilizzo della classe
persona = Persona("Mario", 30)

# Accesso diretto fallirà (Python lo rinomina internamente)
# print(persona.__eta)      # Genera un errore: AttributeError

# Accesso con il getter funzionerà
print(persona.get_eta())  # Output: 30
