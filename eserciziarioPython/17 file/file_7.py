"""
Scrivi una funzione rimuovi_linee_vuote(nome_file) che prende il nome di un file,
rimuove tutte le linee vuote dal file e salva il risultato nello stesso file.
"""

def rimuovi_linee_vuote(nome_file):
    var1=open(nome_file,"r")
    var2=var1.readlines()
    lista=[]
    for linea in var2:
        if linea.strip()!="":
            lista.append(linea)
    var3=open(nome_file,"w")
    var4=var3.writelines(lista)
    return "Linee non vuote aggiunte"

print(rimuovi_linee_vuote('file.txt'))

