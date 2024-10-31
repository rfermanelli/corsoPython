"""
Data una lista di dizionari STUDENTI di 10 elementi strutturata con:
NOME, VOTO1, VOTO2 e VOTO3, caricare in una seconda lista di dizionari MEDIA, strutturata con:
 NOMEALUNNO e VOTOMEDIO e visualizzare l’alunno con la media più alta.
"""

import random

studenti = []
media = []

for indice in range(10):
    studenti.append({'nome': 'studente' + str(indice +1), 'voto1': random.randint(18, 30), 'voto2': random.randint(18, 30), 'voto3': random.randint(18, 30)})

print(studenti)

for indice in range(0, len(list(studenti[indice]))):
    voto_medio = 0
    media_voto = 0
    for chiave in studenti[indice].keys():

        if chiave == 'nome':
            media.append({chiave: studenti[indice][chiave]})
        else:
            media_voto = media_voto + 1
            voto_medio = voto_medio + studenti[indice][chiave]

    voto_medio = voto_medio / media_voto
    media[indice].setdefault('voto_medio', voto_medio)


print(media)
