class RangeError(IndexError):
    pass


class Collection:
    def get(self, index):
        if not (1 <= index <= 10):
            raise RangeError
        return 42


stuff = Collection()
try:
    print(stuff.get(1))
    print(stuff.get(0))
except RangeError:
    pass
except ValueError as error:
    print("failure")
except IndexError:
    print('aho ma che fai?')
#

class MyError(ArithmeticError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    x = 1
    z = 0
    if z == 0:
        raise MyError('KO')
except MyError as err:
    print(err)




