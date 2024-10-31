import modulo_B_1
print(modulo.f(10, lambda x: x ** 2))
#

import modulo_B_1 as p
print(p.f(10, lambda x: x ** 2))
#

from modulo_B_1 import f
print(f(10, lambda x: x ** 2))
#

from modulo_B_1 import *
print(f(10, lambda x: x ** 2))
#