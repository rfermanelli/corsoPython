"""
Scrivi una funzione leggi_file(nome_file) che prende il nome di un file come argomento
e stampa il contenuto del file al contrario eliminando le parole con meno di tre caratteri
"""

def leggi_file(nome_file):
    file = open(nome_file)
    list_file = file.readlines()
    list_file_stampa = []

    for parola in list_file:
        if len(parola.strip()) > 3:
            list_file_stampa.append(parola.strip())

    file.close()
    list_file_stampa = list_file_stampa[::-1]
    return list_file_stampa

print(leggi_file('file.txt'))