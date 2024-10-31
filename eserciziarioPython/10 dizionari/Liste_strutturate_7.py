"""
Dato una lista strutturata AUTOMOBILI [70] (MARCA, CILINDRATA, COLORE, PREZZO),
caricare in una seconda lista ECONOMICHE la MARCA e il COLORE di tutte le auto
il cui PREZZO risulta inferiore a 10000 euro.
Verificare se tra le auto economiche compaiono le case automobilistiche “Fiat” e “Opel”
e notificare il tutto con un messaggio riportando anche il numero totale delle auto economiche
e il numero totale delle suddette case produttrici.
"""

automobili=[{"Marca":"Bmw","Cilindrata":4000,"Colore":"Rosso","Prezzo":5000},{"Marca":"Mercedes","Cilindrata":5000,"Colore":"Blu","Prezzo":3800},{"Marca":"Fiat","Cilindrata":4900,"Colore":"Arancione","Prezzo":70000},{"Marca":"Opel","Cilindrata":3000,"Colore":"Rosso","Prezzo":3978}]
economiche=[]
conteggio1=0
conteggio2=0
for i in automobili:
    if i["Prezzo"]<10000:
        if i["Marca"]=="Fiat" or i["Marca"]==("Opel"):
            economiche.append({i["Marca"]: i["Colore"]})
            conteggio2=conteggio2+1
            conteggio1=conteggio1+1
        else:
            economiche.append({i["Marca"], i["Colore"]})
            conteggio1=conteggio1+1
print("Il conteggio delle auto economiche è:",conteggio1)
print("Il conteggio delle auto economiche fiat o opel è:",conteggio2)
print(economiche)