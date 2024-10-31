"""
Data una lista di dizionari STUDENTI di 10 elementi strutturata con:
NOME, VOTO1, VOTO2 e VOTO3, caricare in una seconda lista di dizionari MEDIA, strutturata con:
 NOMEALUNNO e VOTOMEDIO e visualizzare l’alunno con la media più alta.
"""

lista=[{"Nome":"Gianfranco","Voto1":9,"Voto2":7,"Voto3":8},{"Nome":"Giacomo","Voto1":4,"Voto2":7,"Voto3":8},{"Nome":"Carlo","Voto1":9,"Voto2":8,"Voto3":6},{"Nome":"Giovanni","Voto1":8,"Voto2":7,"Voto3":10},{"Nome":"Girolamo","Voto1":7,"Voto2":9,"Voto3":8},{"Nome":"Francesco","Voto1":4,"Voto2":8,"Voto3":9},{"Nome":"Francesca","Voto1":5,"Voto2":6,"Voto3":9},{"Nome":"Giovanna","Voto1":9,"Voto2":8,"Voto3":6},{"Nome":"Roberto","Voto1":2,"Voto2":6,"Voto3":9}]

lista2=[]
lista3=[]
for i in range(0, len(lista)):
    media=(lista[i]["Voto1"]+lista[i]["Voto2"]+lista[i]["Voto3"])/3
    lista2.append({"NomeAunno":lista[i]["Nome"],"VotoMedio":media})
    lista3.append(media)

alunno = []
voto = []

for i in range(0, len(lista2)):
    alunno.append(lista2[i]['NomeAunno'])
    voto.append(lista2[i]['VotoMedio'])

voto_migliore = voto.index(max(voto))
print(alunno[voto_migliore])