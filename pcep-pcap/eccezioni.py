try:
    x = int(input("Divisore: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("Non puoi dividere per zero.")
except ValueError:
    print("Il divisore deve essere un numero.")
except:
    print("Hai fatto tutto bene ma qualcosa non ha funzionato")
else:
    print('Bravo')
finally:
    print('Ciao')

print("Fine.")