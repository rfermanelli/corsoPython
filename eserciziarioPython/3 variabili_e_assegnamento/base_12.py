"""
Dati in input 15 numeri,
sommare i primi 5 e moltiplicare i restanti 10
non effettuando il prodotto se un elemento è 0,
cioè passare all’elemento successivo.
"""

somma=0
x=0
prodotto=1
for i in range(15):
    num1=int(input("Inserire un numero:"))
    x=x+1
    if x <6:
        somma=somma+num1
    else:
        if num1!=0:
            prodotto=prodotto*num1
        else:
            continue
print("Il prodotto è:",prodotto)
print("La somma è:",somma)

