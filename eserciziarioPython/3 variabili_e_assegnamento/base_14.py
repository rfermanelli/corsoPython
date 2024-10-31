"""
Sfruttando l’operatore %, dato un numero rappresentante un anno A.C. o D.C.,
determinare se è un anno bisestile.
"""

anno=int(input("Inserire un anno A.C. o D.C.: "))
if anno % 4==0:
    print("L' anno",anno,"è bisestile")