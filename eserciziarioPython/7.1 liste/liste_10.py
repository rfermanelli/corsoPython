"""
Dato un numero in input in notazione binaria
convertirlo in notazione decimale.
"""

numero=int(input("inserisci numero decimale: "))

spazio = ""
while numero >0:
    y = numero % 2
    spazio = str(y) +spazio
    numero = numero // 2
print (spazio)
