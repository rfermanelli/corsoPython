"""
Scrivi una funzione parole_piu_lunghe_di_n(testo, n) che prende una stringa testo
e un intero n, e restituisce una lista di parole che hanno più di n caratteri.
"""
def parole_piu_lunghe_di_n(testo,n):
    parole=testo.split()
    lista=[]
    for i in parole:
        if len(i)>n:
            lista.append(i)
    return lista
print(parole_piu_lunghe_di_n("ciaaoo sono tommasoo e vengo da romania",5))

