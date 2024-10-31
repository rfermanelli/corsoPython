# la parola chiave yield per costruire un iteratore
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v, end=' ')
print()

# un iteratore yield per costruire una list comprehension
powers_of_2_list =[p for p in powers_of_2(8)]
print(powers_of_2_list)

# la funzione list()
powers_of_2_listt = list(powers_of_2(3))
print(powers_of_2_listt)

# l'operatore in
for i in range(20):
    if i in powers_of_2(4):
        print(i, end=' ')

# list comprehension con una espressione condizionale
the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)
#
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)
