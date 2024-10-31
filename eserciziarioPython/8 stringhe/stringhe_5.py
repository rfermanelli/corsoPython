"""
Scrivi una funzione anagrammi(parola1, parola2) che prende due stringhe e
restituisce True se sono anagrammi l'una dell'altra, False altrimenti.
"""
def anagrammi(parola1,parola2):
    lista1=list(parola1)
    lista2=list(parola2)
    lista3=[]
    lista4=[]
    if len(parola1)==len(parola2):
        for i in lista1:
            if i in lista2:
                lista3.append(i)
        for n in lista2:
            if n in lista1:
                lista4.append(n)
        if sorted(lista3) == sorted(lista4):
            y = print("Le due parole sono anagrammi")
        else:
            y = print("Le due parole non sono anagrammi")
    else:
        y=print("Le due parolo non sono anagrammi")

    return y
print(anagrammi("f ciao","caio"))

