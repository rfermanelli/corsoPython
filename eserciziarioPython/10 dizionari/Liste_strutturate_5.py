"""
Data la lista DIP strutturata con: REPARTO, MATRICOLA, ORESETT, di 10 elementi,
visualizzare la MATRICOLA e le ORESETT dei dipendenti che hanno lavorato più di 40 ore
e successivamente visualizzare il numero totale di questi dipendenti e il totale ore di straordinario.
"""

DIP=[{"Reparto":"Economia","Matricola":326,"Ore":66},{"Reparto":"Finanza","Matricola":435,"Ore":23},{"Reparto":"Statistica","Matricola":328,"Ore":43},{"Reparto":"Logistica","Matricola":765,"Ore":98},{"Reparto":"Operaio","Matricola":437,"Ore":63},{"Reparto":"Trasporto","Matricola":267,"Ore":59}]
dipendenti=[]

straordinario=0
for i in DIP:
    if i["Ore"]>40:
        straordinario=straordinario+i["Ore"]-40
        """
        dict_appo = {}
        dict_appo['Matricola'] = i['Matricola']
        dict_appo['Ore'] = i['Ore']
        """
        dipendenti.append({i["Matricola"]: i["Ore"]})

print(dipendenti)

print("I dipendenti che lavorano più di 40 ore sono:",len(dipendenti))
print("Il totale delle ore straordinario è: ",straordinario)


