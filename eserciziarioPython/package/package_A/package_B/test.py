import platform

print(platform.platform(terse=True))
print(platform.processor())
print(platform.machine())
print(platform.system())
print(platform.architecture())
print(platform.python_compiler())
print(platform.release())
#

l = [3, 2, 1, 0]
l_2 = l[::2]
print(l_2)
l.sort()
print(l)
l = l[::]
print(l)
l = l[::-1]
print(l)
l_1 = l[1::1]
print(l_1)
#

s = '--GfB89JUUYnhgf--'
print(s.find('B8aa'))
print(s.rfind('UUc'))
print(s.index('9J'))
print(s.lstrip())
print(s.rstrip())
print(s.join(['ecco', 'momo']))
print(s.split())
print(s.split('--'))
#

s_1 = 'le vie Del Signore Sono infinite'
print(s_1.capitalize())
print(s_1.title())
print(s_1.isalnum())
print(s_1.isdigit())
print(s_1.isalpha())
print(s_1.split())
print(s_1.split(' ', len(s_1)))
print(s_1.isupper())
print(s_1.islower())
print(s_1.replace('Del', 'Di', 1))
print(s_1.count('el', 9, 100))
print(s_1.index('Del', 4))
print(s_1.center(150, '-'))
print(s_1.endswith('aho', 3, 9))
print(s_1.endswith('nite', -4, len(s_1)))
print(s_1.startswith('le', 0, 10))
print(s_1.isspace())
print(s_1.lower())
print(s_1.upper())
print(s_1.swapcase())
#

import modulo_B_1
print(dir(modulo))
print((modulo.f(10, lambda x: x ** 10)))
#

import sys
print(sys.path)
#

import math
print(math.ceil(7))
print(math.floor(7))
print(math.ceil(7.56))
print(math.floor(7.56))
print(math.trunc(9.56))
print(math.trunc(9))
print(math.factorial(10))
print(math.hypot(4, 3))
print(math.pow(2,3))
print(math.hypot(4, 3) == math.sqrt(math.pow(4, 2) + math.pow(3, 2)))
#

import random
print(random.seed(0))
print(random.random()) # 0 <= x < 1
print(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random.choice((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)))
print(type(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(random.sample((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 5))


