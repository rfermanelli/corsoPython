def leggi_intero(prompt, min, max):
    try:
        intero = input(prompt + 'compreso tra: ' + str(min) + ' e ' + str(max) + ': ')
        assert int(intero) >= min and int(intero) <= max
        return intero
    except ValueError:
        return ('L\'input non è un valore numerico')
    except AssertionError:
        return ('Il numero deve essere un intero compreso tra ' + str(min) + ' e ' + str(max))

v = leggi_intero("Numero intero", -10, 10)

print("Il numero è:", v)