"""
Acquisire dalla tastiera 10 numeri, caricarli in una lista e
successivamente visualizzare il numero più piccolo e il numero più grande
caricati nella lista. (Non bisogna fare nessun ordinamento).
"""

lista=[]
for i in range(10):
    num=int(input("Inserire numero: "))
    lista.append(num)

print(lista)
print("Il massimo numero della lista è:",max(lista))
print("Il minimo numero della lista è:",min(lista))