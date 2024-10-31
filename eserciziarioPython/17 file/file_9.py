"""
Scrivi una funzione cerca_e_sostituisci(nome_file, parola_cerca, parola_sostituisci)
che prende il nome di un file, una parola da cercare e una parola da sostituire,
e sostituisce tutte le occorrenze della parola cercata con la parola sostituita nel file.
"""

def cerca_e_sostituisci(nome_file, parola_cerca, parola_sostituisci):
    var1=open(nome_file,"r")
    var2=var1.read()
    var3=var2.replace(parola_cerca,parola_sostituisci)
    var4=open(nome_file,"w")
    var5=var4.write(var3)
    return "completato"


print(cerca_e_sostituisci('file.txt', 'thor', 'pinocchio'))


