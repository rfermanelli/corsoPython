"""
Acquisire 2 numeri dalla tastiera corrispondenti
alla base e all’altezza di un rettangolo e
visualizzarne l’area e il perimetro.
"""

base=int(input("inserire un numero per la base: "))
altezza=int(input("inserire un numero per l'altezza:"))
print("L'area del rettangolo corrisponde a :"+str(base*altezza))
print("il perimetro del rettangolo corrisponde a :"+str((base+altezza)*2))