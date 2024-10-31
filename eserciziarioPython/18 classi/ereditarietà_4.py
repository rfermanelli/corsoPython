class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.supVar = 12


obj = Sub()

print(obj.supVar)
