class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " dice: Woof!"
class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Non fuggire, piccola pecorella!"
class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " Rimani dove sei, invasore!"

rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")

print(rocky)
print(luna)

