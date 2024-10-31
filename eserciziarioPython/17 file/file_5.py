"""
Scrivi una funzione copia_file(nome_file_sorgente, nome_file_destinazione) che prende il nome di un
file sorgente e un nome di un file di destinazione,
e copia il contenuto del file sorgente nel file di destinazione.
"""

def copia_file(nome_file_sorgente, nome_file_destinazione):
    sorgente=open(nome_file_sorgente, 'r')
    var1=sorgente.read()
    destinazione=open(nome_file_destinazione, 'a')
    destinazione.write(var1)
    return "Il file è stato copiato"

print(copia_file('file.txt', 'file_d.txt'))

