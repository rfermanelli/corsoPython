"""
 Data la lista strutturata Dip, caricare in una lista ArDip di 50 elementi
 la matricola e le ore settimanali dei dipendenti di un reparto richiesto dalla tastiera
 e infine visualizzare il contenuto dell’array così caricato.
"""

dipendenti = [
    {
        "matricola": "001",
        "reparto": "Amministrazione",
        "ore_settimanali": 40
    },
    {
        "matricola": "002",
        "reparto": "Vendite",
        "ore_settimanali": 35
    },
    {
        "matricola": "003",
        "reparto": "Produzione",
        "ore_settimanali": 45
    },
    {
        "matricola": "004",
        "reparto": "Logistica",
        "ore_settimanali": 38
    },
    {
        "matricola": "005",
        "reparto": "Ricerca e Sviluppo",
        "ore_settimanali": 42
    }
]
ardip=[]
reparto=input("Che reparto ti interessa?: ")
for i in dipendenti:
    if i["reparto"]==reparto:
        ardip.append(i)
print(ardip)