"""
Dati in input da tastiera due numeri,
se il primo risulta essere il doppio del secondo
visualizzarne la differenza altrimenti visualizzarne la somma
"""

num1=int(input("inserire il primo numero:"))
num2=int(input("inserire il secondo numero:"))
if num2*2==num1:
    print(str(num1-num2))
else:
    print(str(num1+num2))