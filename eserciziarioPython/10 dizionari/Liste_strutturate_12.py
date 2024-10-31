"""
Data la lista stutturata Dip (Reparto, Matricola, Oresett),
visualizzare la Matricola e le Ore settimanali dei dipendenti che hanno lavorato più di 40 ore
e infine visualizzare il numero totale di questi dipendenti e il totale delle ore di straordinario.
"""

DIP=[{"Reparto":"Economia","Matricola":326,"Ore":66},{"Reparto":"Finanza","Matricola":435,"Ore":23},{"Reparto":"Statistica","Matricola":328,"Ore":43},{"Reparto":"Logistica","Matricola":765,"Ore":98},{"Reparto":"Operaio","Matricola":437,"Ore":63},{"Reparto":"Trasporto","Matricola":267,"Ore":59}]
dipendenti=[]

straordinario=0
for i in DIP:
    if i["Ore"]>40:
        straordinario=straordinario+i["Ore"]-40
        dipendenti.append({i["Matricola"],i["Ore"]})
print(dipendenti)
print("I dipendenti che lavorano più di 40 ore sono:",len(dipendenti))
print("Il totale delle ore straordinario è: ",straordinario)


