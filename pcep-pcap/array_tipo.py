s = lambda x, y: '0123456789'[x:y]
print(s(0,6))
#

t_1 = (30, 1)
t_2 = (30, 0)
print(t_1 > t_2)
#

l_1 = [0, 1, 3, 'b']
l_2 = [0, 1, 3, 'c']
print(l_1 > l_2)
#

import collections
import types

d_1 = collections.defaultdict(lambda : None)
v = d_1.get('0')
print(v)
d_1['1'] = 1
d_1_readonly = types.MappingProxyType(d_1)
d_1['1'] = 0
#d_1_readonly['1'] = 1
#

import array

arr_1 = array.array('f', (1, 3, 5, 6.9))
arr_2 = arr_1

print(arr_1.__eq__(arr_2))








