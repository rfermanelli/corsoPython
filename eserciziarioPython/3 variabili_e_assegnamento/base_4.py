"""
Acquisire tre numeri dalla tastiera e
visualizzare il numero più grande.
"""
num1=int(input("inserire il primo numero :"))
num2=int(input("inserire il secondo numero :"))
num3=int(input("inserire il terzo numero :"))
if num1>num2 and num1>num3:
    print(str(num1)+" è il numero più grande")
elif num2>num1 and num2>num3:
    print(str(num2)+" è il numero più grande")
else:
    print(str(num3)+" è il numero più grande")