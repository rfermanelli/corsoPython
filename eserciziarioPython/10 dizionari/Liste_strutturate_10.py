"""
Scrivi una funzione che prende in input un dizionario di valori interi positivi
e un valore soglia intero positivo,
e restituisce un nuovo dizionario che contiene solo le coppie chiave-valore
dove il valore è maggiore della soglia.
"""

diz1={"ciao":2,"buongiorno":3,"salve":4}

soglia=int(input("Inserire un valore soglia: "))

diz2={}
for k,v in diz1.items():
    if v > soglia:
        diz2[k]=v
print(diz2)

