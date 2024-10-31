"""
Data la lista PRODVEN (CODICE, PREZZO, IVA, QTAVENDTA) di 200 elementi,
visualizzare il CODICE e il totale in euro dei prodotti di cui sono stati venduti più di 10 pezzi
e memorizzare in una lista di nome PIU [30] il CODICE e la QTAVENDUTA
di tutti i prodotti di cui sono stati venduti più di 50 pezzi.
"""

PRODVEN = [
    {"CODICE": "P001", "PREZZO": 100, "IVA": 22, "QTAVENDTA": 10},
    {"CODICE": "P002", "PREZZO": 200, "IVA": 22, "QTAVENDTA": 55},
    {"CODICE": "P003", "PREZZO": 150, "IVA": 10, "QTAVENDTA": 88},
    {"CODICE": "P004", "PREZZO": 250, "IVA": 22, "QTAVENDTA": 3},
    {"CODICE": "P005", "PREZZO": 300, "IVA": 10, "QTAVENDTA": 2},
    {"CODICE": "P006", "PREZZO": 180, "IVA": 22, "QTAVENDTA": 77}]
totale=0
piu=[]
for i in PRODVEN:
    if i["QTAVENDTA"] >10:
        totale=totale+i["PREZZO"]*i["QTAVENDTA"]-i["IVA"]
        print("L'articolo codice",i["CODICE"],"ha generato un totale di",totale, "EURO")
    if i["QTAVENDTA"]>50:
        piu.append({i["CODICE"]:i["QTAVENDTA"]})
print(piu)