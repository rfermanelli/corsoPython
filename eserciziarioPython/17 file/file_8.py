"""
Scrivi una funzione unisci_file(lista_file, file_destinazione) che prende una lista di nomi di file
e un nome di file di destinazione,
e unisce il contenuto di tutti i file nella lista in un unico file di destinazione.
"""

def unisci_file(lista_file, file_destinazione):
    var1=open(file_destinazione,"w")
    for nome in lista_file:
        var2=open(nome,"r")
        for riga in var2:
            var1.write(riga)

    return "Completato"


lista_file =['file.txt', 'file_d.txt']
print(unisci_file(lista_file, 'file_destinazione.txt'))