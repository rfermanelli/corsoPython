"""
Scrivi una funzione che prende in input due dizionari e
restituisce un nuovo dizionario che contiene tutte le chiavi di entrambi i dizionari.
Se una chiave è presente in entrambi,
il valore nel nuovo dizionario deve essere la somma dei valori dei due dizionari originali.
"""

diz1={1:"ciao",2:"buongiorno",3:"salve"}

diz2={2:"ola",3:"ciao",4:"salve"}

diz3=diz2.copy()

for k,v in diz1.items():
    if k in diz3:
        diz3[k]=diz3[k]+v
    else:
        diz3[k]=v
print(diz3)