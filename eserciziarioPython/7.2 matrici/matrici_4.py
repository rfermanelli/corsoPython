"""
Data una matrice 6x8 di numeri interi,
stampare l’indice della colonna
con il maggior numero di elementi dispari.
"""

matrice=[]
conteggio=[0,0,0,0,0,0]
n=0

for i in range(1, 7):
    riga=[]
    for j in range(1, 9):
        riga.append(i * j)
    matrice.append(riga)

for i in range(len(matrice)):
    riga = matrice[i]
    for j in range(len(riga)):
        if riga[j]%2==1:
            conteggio[i]=conteggio[i]+1
    n=n+1

print(matrice)
print(conteggio)
print(max(conteggio))


