"""
Creare una matrice 10x10 con i valori della tavola pitagorica,
quindi richiedere all’utente un numero tra 0 e 9 e
visualizzare i valori della tabellina.
"""

matrice=[]
for i in range(1, 11):
    riga=[]
    for j in range(1, 11):
        riga.append(i * j)
    matrice.append(riga)

numero=int(input("Di quale numero vuoi sapere la tabellina?: "))
if numero <= 10 and numero >= 1:
    print(matrice[numero - 1])


