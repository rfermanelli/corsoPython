"""
Scrivi una funzione frequenza_caratteri(testo) che prende una stringa e
restituisce un dizionario con la frequenza di ogni carattere presente nella stringa.
"""
def frequenza_caratteri(stringa):
    mydict={}


    for i in stringa:
        if i not in mydict:
            mydict[i]=1

        else:
            mydict[i]=mydict[i]+1
    return mydict

print(frequenza_caratteri("vamoscaraco"))