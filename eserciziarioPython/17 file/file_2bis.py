"""
Scrivi una funzione scrivi_file(nome_file, testo) che prende il nome di un file e una stringa di testo,
e scrive la stringa nel file prima della prima parola.
"""

def scrivi_file(nome_file,testo):
    variabile1=open(nome_file,"r")
    variabile2=open(nome_file,"a")
    variabile2.write(testo + variabile1)
    return "Il testo è stato aggiunto"

print(scrivi_file('file.txt', 'dottor strange'))
