"""
Acquisire 3 numeri dalla tastiera e
visualizzare il numero più grande,
il numero medio e
il numero più piccolo
senza utilizzare strutture iterative.
"""

num1=int(input("inserire un numero: "))
num2=int(input("inserire un numero: "))
num3=int(input("inserire un numero: "))
if num1>num2 and num1>num3 and num2>num3:
    print(str(num1)+" è il numero più grande")
    print(str(num2)+" è il numero intermedio")
    print(str(num3)+" è il numero più piccolo")
elif num1>num2 and num1>num3 and num3>num2:
    print(str(num1) + " è il numero più grande")
    print(str(num3) + " è il numero intermedio")
    print(str(num2) + " è il numero più piccolo")

elif num2>num1 and num2>num3 and num1>num3:
    print(str(num2)+" è il numero più grande")
    print(str(num1)+" è il numero intermedio")
    print(str(num3)+" è il numero più piccolo")
elif num2>num1 and num2>num3 and num3>num1:
    print(str(num2)+" è il numero più grade")
    print(str(num3)+" è il numero intermedio")
    print(str(num1)+" è il numero più piccolo")
elif num3>num1 and num3>num2 and num1>num2:
    print(str(num3)+" è il numero più grande")
    print(str(num1)+" è il numero intermedio")
    print(str(num2)+" è il numero più piccolo")
else:
    print(str(num3)+" è il numero più grande")
    print(str(num2)+" è il numero intermedio")
    print(str(num1)+" è il numero più piccolo")
