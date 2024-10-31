stringa = input('Stringa da controllare: ')

stringa_lista = list(stringa)
stringa_lista_palindroma = list(stringa)

stringa_lista = ''.join(stringa_lista)

stringa_lista_palindroma = ''.join(stringa_lista_palindroma)

if stringa_lista == stringa_lista_palindroma:
    print('La stringa in input è palindorma')
else:
    print('La stringa in input non è palindorma')

