"""
Scrivi una funzione rimuovi_duplicati(lista) che prende una lista di stringhe
e restituisce una nuova lista con i duplicati rimossi, mantenendo l'ordine originale.
"""
def rimuovi_duplicati(lista):
    senza_duplicati=[]
    for i in lista:
        if i not in senza_duplicati:
            senza_duplicati.append(i)
    return senza_duplicati
print(rimuovi_duplicati(["ciao","tommaso","ciao","jimmy","jimmy", 'ciao']))