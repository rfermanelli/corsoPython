"""
Scrivi una funzione che prende in input un dizionario e
restituisce un nuovo dizionario con chiavi e valori invertiti.
Supponi che tutti i valori siano unici.
"""
def inverti_dizionario(dizionario):

    dizionario_invertito = {}
    dizionario_chiave = list(dizionario.keys())

    dizionario_valore = list(dizionario.values())

    for indice in range(0, len(dizionario_valore)):
        dizionario_invertito[dizionario_valore[indice]] = dizionario_chiave[indice]

    return dizionario_invertito

dizionario = {1: 'uno', 2:'due', 3:'tre'}
print(inverti_dizionario(dizionario))

