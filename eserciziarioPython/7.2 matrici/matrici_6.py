"""
Scrivi una funzione che prende in input due matrici
e calcola il loro prodotto.
Se le matrici non possono essere moltiplicate
(numero di colonne della prima matrice diverso dal numero di righe della seconda matrice),
la funzione deve restituire un messaggio di errore.
"""

matrice1=[[1,2,3],[4,5,6],[7,8,9]]
matrice2=[[1,2],[3,4],[5,6]]
prod = True

for i in range(len(matrice1)):
    if len(matrice1[i]) == len(matrice2):
        continue
    else:
        prod = False
        break

if prod:
    somma1=0
    prodotto=0

    for i in range(len(matrice1[0])):
        for j in range(0, len(matrice2) - 1):
            prodotto=prodotto+matrice1[i][j]*matrice2[i][j]

    print(prodotto)
else:
    print('Le due matrici non sono moltiplicabili')





