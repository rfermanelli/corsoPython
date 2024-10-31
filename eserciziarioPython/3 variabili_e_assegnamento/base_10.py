"""
Calcolare la somma e il prodotto di n numeri dati in input
(chiedere inizialmente quanti numeri si vogliono inserire).
Indicare quindi con un messaggio se la somma è maggiore, minore
o uguale al prodotto.
"""

numeri=int(input("Quanti numeri vuoi inserire? "))
somma=0
prodotto=1
for i in range(numeri):
    num1=int(input("inserire numero: "))
    somma=somma+num1
    prodotto=prodotto*num1
print("Il prodotto è: "+str(prodotto))
print("La somma è: "+ str(somma))
if somma>prodotto:
    print("La somma è maggiore del prodotto")
elif somma<prodotto:
    print("La somma è minore del prodotto")
else:
    print("La somma è uguale al prodotto")

