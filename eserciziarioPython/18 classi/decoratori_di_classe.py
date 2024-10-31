def count(aClass):
    aClass.numInstances= 0
    return aClass


@count
class Spam:
    def __init__(self):
        Spam.numInstances = Spam.numInstances+ 1


@count
class Sub(Spam):
    pass


@count
class Other(Spam):
    def __init__(self):
        Other.numInstances = Other.numInstances+ 1

