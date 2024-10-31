"""
Inserire un numero dalla tastiera
corrispondente ad un mese dell’anno
(se il numero non è valido chiedere di inserire nuovamente un numero)
e visualizzare quale mese è.
"""

mese=int(input("inserire un numero corrispondente ad un mese dell'anno: "))
while mese >12 and mese <1:
    mese=int(input("inserire un numero valido corrispondente a un mese dell'anno"))
if mese == 1:
    print("il mese è gennaio")
elif mese==2:
    print("il mese è febbraio")
elif mese ==3:
    print("il mese è marzo")
elif mese == 4 :
    print("il mese è aprile")
elif mese==5:
    print("il mese è maggio")
elif mese==6:
    print("il mese è giugno")
elif mese==7:
    print("il mese è luglio")
elif mese== 8:
    print("il mese è agosto")
elif mese == 9:
    print("il mese è settembre")
elif mese==10:
    print("il mese è ottobre")
elif mese==11:
    print("il mese è novembre")
else:
    print("il mese è dicembre")
