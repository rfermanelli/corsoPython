"""
Scrivi una funzione che prende in input due stringhe s1 e s2,
di cui s2 è la stringa da cercare in s1;
e restituisce un valore booleano che indica se la stringa s2 è contenuta in s1.
Se s2 è contenuta in s1 allora indicare il punto di partenza di s2 in s1 e la lunghezza di s1 senza s2.
"""

s1=input("Inserire una stringa: ")
s2=input("Inserire una stringa da ricercare in s1: ")

trova=s1.find(s2)
if trova !=-1:
    lungh=len(s1)-len(s2)
    print(True)
    print(int(s1.index(s2)))
else:
    print(False)