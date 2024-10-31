class Super:
    subVar = 1


class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar)
