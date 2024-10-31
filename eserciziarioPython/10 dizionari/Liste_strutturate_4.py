"""
Dati due liste: STUDENTI [120] strutturato con MATRICOLA, CF, NOME, COGNOME
LAVORATORI [46] strutturato con CF, NOME, COGNOME
Caricare una terza lista STUDENTILAVORATORI[?] con CF, NOME, COGNOME
soltanto con gli elementi che risultano essere comuni alle due liste.
"""

lavoratori = [{"CF": "CF001", "Nome": "Mario", "Cognome": "Rossi"},{"CF": "CF004", "Nome": "Giulia", "Cognome": "Esposito"},{"CF": "CF003", "Nome": "Anna", "Cognome": "Bianchi"}]
studenti=[{"Maricola":2345,"CF":"CF001","Nome":"Mario","Cognome":"Rossi"},{"Matricola":2365,"CF":"CF004","Nome":"Giulia","Cognome":"Esposito"},{"CF":"GOI","Nome":"Tommaso","Cognome":"Bertolacci"}]
studlav=[]
for i in lavoratori:
    for c in studenti:
        if c["CF"]==i["CF"]:
            studlav.append([i["CF"],i["Nome"],i["Cognome"]])
print(studlav)