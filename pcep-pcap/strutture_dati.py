#
import array

arr_1 = array.array('f', (1, 8, 5, 6.9))
arr_2 = array.array('d', (0, 1, 2, 3, 4, 5, 6, 7))

try:
    arr_1.__eq__(arr_2)
except:
    print('Il tipo:', str(type(arr_1)), 'non è confrontabile con il tipo:', str(type(arr_2)))
else:
    print('Il tipo:', str(type(arr_1)), 'è confrontabile con il tipo:', str(type(arr_2)))
finally:
    if arr_1.__eq__(arr_2):
        print(True)
    else:
        print(False)
    print('Ordinamento completato')

print(arr_1.__str__())
print(dir(array.array))

import operator
z = operator.add(8, 9)
print(z)





