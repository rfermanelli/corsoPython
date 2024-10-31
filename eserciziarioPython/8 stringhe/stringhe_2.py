"""
Scrivi una funzione che prende in input una stringa e
restituisce la lunghezza della sottostringa più lunga che non contiene caratteri ripetuti.
"""

stringa=input("Inserire una stringa: ")
lista=list(stringa)
lista2=[]
lunga=0
for i in lista:
    if i not in lista2:
        lista2.append(i)
        if len(lista2)>lunga:
            lunga=len(lista2)

    else:

        lista2.clear()
        lista2.append(i)
print(lunga)

