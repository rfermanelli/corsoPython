"""
Data una lista di 15 numeri, acquisire da tastiera un numero
e cercarlo nella lista; se presente visualizzare la sua posizione nell’array.
"""

lista=[]
for i in range(15):
    num=int(input("Inserire numero: "))
    lista.append(num)
print(lista)
numero=int(input("inserire numero da cercare"))
y = lista.index(numero)
print("la posizione di",numero,"nella lista è",y)
