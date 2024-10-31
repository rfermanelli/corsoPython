"""
Data una lista di 18 numeri,
calcolare il prodotto dei numeri in posizione dispari
e la somma dei numeri in posizione pari.
"""

lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
prodotto=1
somma=0
for i in lista[0::2]:
    somma=somma+i

for i in lista[1::2]:
    prodotto = prodotto * i

print("La somma dei numeri pari è:",somma)
print("Il prodotto dei numeri dispari è:",prodotto)
    

