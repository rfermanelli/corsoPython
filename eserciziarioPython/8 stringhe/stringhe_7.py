"""
Scrivi una funzione inversione_parole(frase) che prende una stringa contenente una frase
e restituisce una nuova stringa con l'ordine delle parole invertito.
"""
def inversione_parole(frase):
    y=frase.split()
    lista=[]
    for i in y:
       parole_inverse= i[::-1]
       lista.append(parole_inverse)
    frase_inversa=" ".join(lista)
    return frase_inversa
print(inversione_parole("ciao sono tommaso"))


