"""
Data una matrice 3×3,
richiedere un numero da tastiera e
se presente visualizzare le coordinate delle celle dove si trova,
altrimenti comunicare che non è presente.
"""

matrice=[[1,2,3],[4,5,6],[7,8,9]]
numero=int(input("Digita un numero del quale vuoi trovare le coordinate"))

y=False
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        if matrice[i][j] == numero:
            print("Il numero",numero," si trova nelle coordinate", i,j)
            y=True
            break
if not y:
    print("Numero non trovato")

