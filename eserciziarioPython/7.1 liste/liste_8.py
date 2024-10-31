"""
Data una lista di 10 elementi contenente numeri tra 0 e 9,
contare quante volte ogni numero compare nella lista.
"""

lista=[0,1,3,3,4,9,6,8,8,9]
lista2=[]
conteggio=0
for i in lista:
    if i not in lista2:
        lista2.append(i)
for i in lista2:
    x=lista.count(i)
    print(i,"compare",x,"volte")


