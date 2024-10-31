"""
Data una matrice 10x10,
verificare se la somma degli elementi sulla diagonale principale
coincide con la somma degli elementi sulla diagonale secondaria,
altrimenti indicare quale delle due somme è maggiore.
"""
matrice=[]
somma1=0
somma2=0
n=0
k=-1
for i in range(1, 11):
    riga=[]
    for j in range(1, 11):
        riga.append(i * j)
    matrice.append(riga)
for i in range(len(matrice)):
    somma1=somma1+matrice[i][n]
    n=n+1
for i in range(len(matrice)):
    somma2=somma2+matrice[i][k]
    k=k-1
if somma1 >somma2:
    print("La somma dei numeri sulla diagonale principale è maggiore di quella dei numeri sulla secondaria")
elif somma1==somma2:
    print("La somma delle due diagonali è la stessa")
else:
    print("La somma dei numeri sulla diagonale secondaria è maggiore di quella dei numeri sulla diagonale principale")
