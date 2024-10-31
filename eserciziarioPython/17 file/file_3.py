"""
Scrivi una funzione aggiungi_file(nome_file, testo) che prende il nome di un file e una stringa di testo,
e aggiunge il testo alla fine del file.
"""

def aggiungi_stringa_a_file(nome_file, stringa_da_aggiungere):

    file_da_scrivere = open(nome_file, 'a')
    if file_da_scrivere.mode != 'w':
        stringa_da_aggiungere = '\n' + stringa_da_aggiungere
    file_da_scrivere.write(stringa_da_aggiungere)
    file_da_scrivere.close()

    return 'La stringa in input è stata aggiunta, in append, al file'

print(aggiungi_stringa_a_file('../../pcep-pcap/file.txt', 'vedova nera'))