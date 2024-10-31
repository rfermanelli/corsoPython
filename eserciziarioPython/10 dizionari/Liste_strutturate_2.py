"""
Dato una lista ARTICOLI con i campi:
MARCA, GIACENZA, PREZZO. di 7 elementi, caricare una seconda lista di nome ART con i campi
 MARCA, VALORE (valore = prezzo * giacenza)
 di tutti gli elementi presenti in ARTICOLI il cui VALORE > 150
 e visualizzare infine il VALORE totale complessivo.
"""

Articoli=[{"Marca":"Bmw","Giacenza":4,"Prezzo":34},{"Marca":"Adidas","Giacenza":3,"Prezzo":56},{"Marca":"Nike","Giacenza":8,"Prezzo":47},{"Marca":"Supreme","Giacenza":6,"Prezzo":48}]
art=[]
valore=0
valoretot=0
for i in Articoli:
    valore=i["Giacenza"]*i["Prezzo"]
    valoretot=valoretot+valore

    if valore >150:
        art.append(valore)

print(valore)
print(art)





