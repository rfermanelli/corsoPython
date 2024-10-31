"""
Scrivi una funzione conta_linee(nome_file) che prende il nome di un file e
restituisce il numero di linee presenti nel file.
"""

def conta_linee(frasi):
    var1=open(frasi,"r")
    var2=var1.readlines()
    return "Le linee sono",len(var2)


print(conta_linee('file.txt'))

