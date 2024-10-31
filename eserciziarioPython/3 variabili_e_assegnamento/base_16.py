"""
Acquisire un numero dalla tastiera
quindi calcolare e visualizzare il suo fattoriale.
"""

num1=int(input("Inserire un numero: "))
fattoriale=num1
while fattoriale >1:
    fattoriale=fattoriale-1
    num1=num1*fattoriale

print("Il numero fattoriale:",num1)