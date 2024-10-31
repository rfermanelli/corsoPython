"""
Acquisire una sequenza di numeri naturali che termina con 0
e visualizzare la lunghezza della sotto sequenza crescente
più lunga contenuta nella sequenza di dati acquisiti.
"""

numero_naturale = 0
contatore_precedente = 0
contatore_attuale = 0
scambio = 0

numero_naturale = int(input('input: '))
while numero_naturale != 0:
    if numero_naturale > scambio:
        contatore_attuale = contatore_attuale + 1
    else:
        contatore_precedente = contatore_attuale
        contatore_attuale = 1
    scambio = numero_naturale
    numero_naturale = int(input('input: '))
if contatore_attuale > contatore_precedente:
    print('La sotto sequenza crescente più lunga è di:', contatore_attuale, 'cifre')
else:
    print('La sotto sequenza crescente più lunga è di:', contatore_precedente, 'cifre')


