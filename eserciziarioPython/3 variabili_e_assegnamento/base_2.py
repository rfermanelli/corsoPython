"""
Acquisire un numero intero > di 0 da tastiera e
visualizzare se è pari o dispari avendo a disposizione
solamente le operazioni +, -, *, /.
(Considerare che il tipo num è intero e
che anche la divisione produce un risultato intero).
"""

num1=int(input("inserire un numero maggiore di 0:"))
while num1 < 0:
    num1=int(input("inserire un numero maggiore di 0:"))
var1=num1//2
if var1*2==num1:
    print("il numero è pari")
else:
    print("il numero è dispari")