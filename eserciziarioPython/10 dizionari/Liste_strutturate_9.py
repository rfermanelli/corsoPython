"""
Scrivi una funzione che prende in input un dizionario e
restituisce un nuovo dizionario con chiavi e valori invertiti.
Supponi che tutti i valori siano unici.
"""
def inverti_dizionario(dizionario):
    dizionario2 = {}
    for k,v in dizionario1.items():
        dizionario2[v] = k
    return dizionario2


dizionario1 = {1:"ciao",2:"buongiorno",3:"buonasera",4:"salve"}

print(inverti_dizionario(dizionario1))