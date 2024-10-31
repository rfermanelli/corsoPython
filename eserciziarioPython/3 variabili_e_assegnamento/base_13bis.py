"""
Ricevere in input una sequenza di numeri
che termina con 0 e
visualizzare il numero maggiore che è stato inserito dall’utente.
"""

y=0
num1=int(input("Inserire un numero: "))
while num1 != 0:
    num1=int(input("Inserire un numero: "))
    if num1 >y:
        y=num1
print("Il numero massimo è:",y)

