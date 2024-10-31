f = lambda x: x
print(f(10))

import math
d = {'quadrato': lambda x: x ** 2, 'radice_quadrata': lambda x: math.sqrt(x)}
print(d['quadrato'](6))
print(d['radice_quadrata'](81))


def generator(n):
    for i in range(n):
        yield i


# La funzione map()
lambda_map = map(lambda e: e ** 2, [x for x in generator(10)])
for i in lambda_map:
    print(i, end=' ')
print()


# La funzione filter()
lambda_filter = filter(lambda e: e ** 2 > 10, [x for x in generator(10)])
for i in lambda_filter:
    print(i, end=' ')
