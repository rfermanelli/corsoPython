"""
Scrivi una funzione parole_piu_frequenti(nome_file, n) che prende il nome di un file
e un intero n, e restituisce una lista delle n parole più frequenti nel file, insieme al loro conteggio
"""

def parole_piu_frequenti(nome_file,n):
    var1=open(nome_file,"r")
    var2=var1.read()
    conteggio=var2.count(n)
    return conteggio

print(parole_piu_frequenti('file.txt', 'thor'))