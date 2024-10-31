stringa_1 = input('Stringa n. 1: ')
stringa_2 = input('Stringa n. 2: ')

posizione = 0

for carattere in stringa_1:
    if stringa_2.find(carattere) != -1:
        posizione = posizione + 1

if posizione == len(stringa_1):
    print('La stringa n. 1 è contenuta nella stringa n. 2')
else:
    print('La stringa n. 1 non è contenuta nella stringa n. 2')







