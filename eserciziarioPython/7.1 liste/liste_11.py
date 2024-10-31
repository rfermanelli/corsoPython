"""
Scrivere una funzione chiamata ordina_trasforma_liste che ha come argomento una lista di stringhe (parole). La funzione deve eseguire le seguenti operazioni:
Ordina la lista di parole in ordine crescente;.
Trasforma ogni parola secondo le seguenti regole:
Se la lunghezza della parola è pari, inverti l'ordine dei caratteri.
Se la lunghezza della parola è dispari, sostituisci ogni vocale con il carattere '*'
Infine la funzione deve restituire la lista trasformata.
"""

def ordina_trasforma_liste(lista_di_stringhe):
    print(lista_di_stringhe)
    parole_ordinate = sorted(lista_di_stringhe)
    print(parole_ordinate)

    for parola in parole_ordinate:
        if len(parola) % 2 == 0:
            indice_parola = parole_ordinate.index(parola)
            parola_in_lista = list(parola)
            parola_in_lista.reverse()
            parole_ordinate[indice_parola] = ''.join(parola_in_lista)
            #del(parole_ordinate[indice_parola + 1])

        if len(parola) % 2 == 1:
            indice_parola = parole_ordinate.index(parola)
            for carattere in parola:
                if carattere in ('a', 'e', 'i', 'o', 'u'):
                    p = parola.replace(carattere, '*')
                    parola = p
            parole_ordinate[indice_parola] = parola

    return parole_ordinate

print(ordina_trasforma_liste(["python", 'abaco', "lista", "esercizio", "programmazione", "sfida", "compito"]))