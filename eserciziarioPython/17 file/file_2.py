"""
Scrivi una funzione scrivi_file(nome_file, testo) che prende il nome di un file e una stringa di testo,
e scrive la stringa nel file prima della prima parola.
"""

def scrivi_file(nome_file, stringa_da_aggiungere):

    file_da_scrivere = open(nome_file, 'r')
    lista_da_file = file_da_scrivere.readlines()
    file_da_scrivere.close()
    stringa_da_aggiungere = stringa_da_aggiungere.split(' ',0)
    lista_da_file[:0] = stringa_da_aggiungere + ['\n']
    stringa_da_scrivere = ''.join(lista_da_file)
    file_da_scrivere = open(nome_file, 'w')
    file_da_scrivere.write(stringa_da_scrivere)
    file_da_scrivere.close()

    return 'La stringa in input è stata aggiunta all\'inizio del file'

print(scrivi_file('../../pcep-pcap/file.txt', 'dottor strange'))