"""
Richiedere in input tre numeri che
rappresentino rispettivamente giorno, mese e anno di una data
(senza verificare la correttezza dei numeri)
e verificare la validità della data immessa.
"""

giorno=int(input("Inserire il giorno della data: "))
mese=int(input("Inserire il mese della data: "))
anno=int(input("Inserire l'anno della data: "))
if mese == 2 and anno % 4==0 and giorno <30:
    print("La data è :", giorno,"/",mese,"/",anno)
elif mese ==2 and giorno <29:
    print("La data è :", giorno, "/", mese, "/", anno)
elif mese== 11 or mese == 9 or mese == 4 or mese ==6 and giorno <31:
    print("La data è :", giorno, "/", mese, "/", anno)
elif mese >12 and giorno >31:
    print("La data non è valida")
else:
    print("Data non valida")