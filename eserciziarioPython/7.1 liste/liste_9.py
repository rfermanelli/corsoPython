"""
Dato un numero in input espresso in notazione decimale
convertirlo in notazione binaria.
"""

numero=input("dammi un numero: ")
lista=[]
y=0

while int(numero) in (0, 1):
    lista.append(int(numero))
    numero = input("dammi un numero: ")

for i in range(0, len(lista)):
    y=y+lista[i]*2**((len(lista)-1)-i)

print(y)





