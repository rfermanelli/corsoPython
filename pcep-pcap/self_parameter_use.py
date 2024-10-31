class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)

# istanzio la classe Classy e creo le variabili di istanza del costruttore
obj = Classy()

# creo una variabile di istanza al di fuori del costruttore
obj.var = 3

# invoco il metodo method dell'oggetto obj
obj.method()

###

class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()


obj = Classy()
obj.method()





