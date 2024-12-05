stringa_1 = input('Stringa n. 1: ')
stringa_2 = input('Stringa n. 2: ')

anagramma = 0

if len(stringa_1) == len(stringa_2):
    for carattere in stringa_2:
        if carattere in stringa_1:
            continue
        else:
            anagramma = 1
            break
else:
    anagramma = 1

if anagramma == 0:
    print('La stringa n. 1 è un angramma della stringa n. 2')
else:
    print('La stringa n. 1 non è un angramma della stringa n. 2')


