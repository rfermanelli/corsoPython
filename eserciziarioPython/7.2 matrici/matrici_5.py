"""
Scrivi una funzione che prende in input una matrice quadrata
(lista di liste) e la ruota di 90 gradi in senso orario.
La funzione deve restituire la matrice ruotata.
"""

matrice=[]

for i in range(1, 4):
    riga=[]
    for j in range(1, 4):
        riga.append(i * j)
    matrice.append(riga)

print(matrice)

matrice_ruotata = [[], [], []]

for i in range(len(matrice)):
    for j in range(len(matrice)):
        matrice_ruotata[j].append(matrice[i][j])

for i in range(len(matrice_ruotata)):
    matrice_ruotata[i].reverse()

print(matrice_ruotata)

