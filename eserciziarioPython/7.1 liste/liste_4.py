"""
Data una lista di 16 numeri,
caricare una seconda lista con tutti i numeri con indice dispari
e una terza lista con tutti i numeri con indice pari
e infine visualizzare la media aritmetica dei valori presenti
nelle prime 5 posizioni della seconda e della terza lista.
"""

lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
lista2=[]
lista3=[]
somma2=0
somma3=0

for i in lista[1::2]:
    lista2.append(i)

for i in lista[0::2]:
    lista3.append(i)

for i in lista2[:5]:
    somma2=somma2+i

for i in lista3[:5]:
    somma3=somma3+i

print("La media aritmetica è:",(somma2+somma3)/10)
