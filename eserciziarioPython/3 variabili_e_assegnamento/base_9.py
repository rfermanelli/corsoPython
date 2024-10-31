"""
Risolvere l’esercizio del numero pari o dispari
con il metodo delle sottrazioni successive.
"""

num1=int(input("Inserire un numero intero:"))
x=num1
while (x>0):
    x=x-2
if x == 0:
    print("Il numero è pari")
else:
    print("Il numero è dispari")