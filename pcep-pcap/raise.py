def cattiva_funzione(n):
    raise ZeroDivisionError


try:
    cattiva_funzione(0)
except ArithmeticError:
    print("Che cosa?! Un errore?")

print("Fine.")
#
def cattiva_funzione(n):
    try:
        return n / 0
    except:
        print("Di nuovo lo stesso errore?")
        raise

try:
    cattiva_funzione(0)
except ArithmeticError:
    print("Si, di nuovo!")

print("Fine.")
