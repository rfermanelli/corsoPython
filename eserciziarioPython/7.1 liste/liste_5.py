"""
Data una lista di 20 numeri,
caricare in una seconda lista gli ultimi 5 numeri presenti nella prima lista
e in una terza lista i primi 10 numeri della prima lista,
dopodiché visualizzare il contenuto delle due liste riempite.
"""

lista1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista2=[]
lista3=[]
for i in lista1[-6:]:
    lista2.append(i)
for i in lista1[:10]:
    lista3.append(i)
print("Il contenuto della seconda lista è:",lista2)
print("Il contenuto della terza lista è:",lista3)


