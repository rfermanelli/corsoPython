"""
Richiedere in input 4 numeri.
Visualizzare un messaggio che indichi
se tra i 4 numeri inseriti almeno uno supera il valore 1000.
"""

num1=int(input("inserire il primo numero: "))
num2=int(input("inserire il secondo numero:"))
num3=int(input("inserire il terzo numero: "))
num4=int(input("inserire il quarto numero: "))
if num1>1000 or num2>1000 or num3 >1000 or num4>1000:
    print("Almeno un numero supera il valore 1000")