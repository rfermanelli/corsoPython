"""
Scrivi una funzione aggiungi_file(nome_file, testo) che prende il nome di un file e una stringa di testo,
e aggiunge il testo alla fine del file.
"""


def aggiungi_file(nome_file, testo):
    variabile=open(nome_file,"a")
    variabile.write(testo)
    return "il file è stato aggiunto"

print(aggiungi_file('file.txt', 'ironman'))
