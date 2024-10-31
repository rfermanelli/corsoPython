list_comprehension = [e for e in range(10)]
print(list_comprehension)

list_comprehension = [e for e in range(10) if e % 2 == 0]
print(list_comprehension)

list_comprehension = []
for e in range(10):
    list_comprehension.append(0 if e % 2 == 0 else 1)
print(list_comprehension)
