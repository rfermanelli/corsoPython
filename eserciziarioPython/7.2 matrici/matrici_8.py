def somma_minima_percorso(matrice):
    # Se la matrice è vuota, restituisci 0
    if not matrice or not matrice[0]:
        return 0

    # Ottieni il numero di righe e colonne
    righe = len(matrice)
    colonne = len(matrice[0])

    # Crea una matrice DP per memorizzare le somme minime fino a ciascuna cella
    dp = [[0] * colonne for _ in range(righe)]

    # Inizializza la cella di partenza (in alto a sinistra)
    dp[0][0] = matrice[0][0]

    # Riempie la prima riga (ci si può muovere solo da sinistra verso destra)
    for j in range(1, colonne):
        dp[0][j] = dp[0][j - 1] + matrice[0][j]

    # Riempie la prima colonna (ci si può muovere solo dall'alto verso il basso)
    for i in range(1, righe):
        dp[i][0] = dp[i - 1][0] + matrice[i][0]

    # Riempie il resto della matrice DP
    for i in range(1, righe):
        for j in range(1, colonne):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrice[i][j]

    # Restituisce la somma minima per raggiungere l'ultima cella (in basso a destra)
    return dp[righe - 1][colonne - 1]


# Esempio di utilizzo
matrice = [
    [7, 3, 10, 0],
    [8, 9, 1, 0],
    [0, 0, 80, 0],
    [0, 0, 100, 1]
]

print(somma_minima_percorso(matrice))  # Output: 7
