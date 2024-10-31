class SuperClasse:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(SuperClasse):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)


