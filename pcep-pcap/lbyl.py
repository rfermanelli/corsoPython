import os

def leggi_file(nome_file):
    # Controlla se il file esiste
    if not os.path.exists(nome_file):
        print(f"Errore: il file '{nome_file}' non esiste.")
        return
    # Controlla se il percorso è un file (e non una directory)
    if not os.path.isfile(nome_file):
        print(f"Errore: '{nome_file}' non è un file.")
        return
    # Controlla se il file è leggibile
    if not os.access(nome_file, os.R_OK):
        print(f"Errore: il file '{nome_file}' non è leggibile.")
        return
    # Se tutti i controlli sono passati, leggi il file
    with open(nome_file, 'r') as file:
        contenuto = file.read()
        print("Contenuto del file:")
        print(contenuto)

# Esempio di utilizzo
nome_file = 'testo.txt'
leggi_file(nome_file)
                                                                               
