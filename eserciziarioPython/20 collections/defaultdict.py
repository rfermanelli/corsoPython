from collections import defaultdict

d = defaultdict(lambda: 'la chiave è assente')

print(d[0])

d[0] = 'zero'

print(d[0])


