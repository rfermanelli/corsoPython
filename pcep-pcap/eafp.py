def leggi_file(nome_file):
    try:
        with open(nome_file, 'r') as file:
            contenuto = file.read()
            print("Contenuto del file:")
            print(contenuto)
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non esiste.")
    except IsADirectoryError:
        print(f"Errore: '{nome_file}' è una directory, non un file.")
    except PermissionError:
        print(f"Errore: il file '{nome_file}' non è leggibile.")
    except Exception as e:
        print(f"Errore sconosciuto: {e}")

# Esempio di utilizzo
nome_file = 'testo.txt'
leggi_file(nome_file)


