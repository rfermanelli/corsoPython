"""
Scrivi una funzione leggi_file(nome_file) che prende il nome di un file come argomento
e stampa il contenuto del file al contrario eliminando le parole con meno di tre caratteri
"""

def leggi_file(nome_file):
    file=open(nome_file,"r")
    t=file.read()
    frasi=t.split()
    lista=[]
    for parola in frasi:
        if len(parola)>=3:
            lista.append(parola)
    lista1=" ".join(lista)
    contrario=lista1[::-1]
    return contrario

print(leggi_file('file.txt'))
