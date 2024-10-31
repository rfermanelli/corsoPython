"""
Scrivi una funzione che prende in input una stringa
e restituisce la sottostringa palindroma più lunga.
Se ci sono più sottostringhe di massima lunghezza,
restituisci la prima che appare.
Si assuma che le sottostringhe siano separate da uno spazio.
"""

stringa=input("Inserire una stringa di parole: ")
copia=stringa.split()
lista=stringa.split()
lista1=[]
for i in lista:
    y=i[::-1]
    if y in copia:
        lista1.append(i)
stringa_lunga=""
for n in lista1:
    if len(n)>len(stringa_lunga):
        stringa_lunga=n
print(stringa_lunga)

