"""
Lette in input due liste rispettivamente di lunghezza 20 e 10 senza ripetizioni,
stampare tutti gli elementi in comune.
"""

lista1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista2=[1,2,3,4,5,6,7,8,9,10]
for i in lista1:
    if i in lista2:
        print("L'elemento",i,"è presente ache in lista2")
        