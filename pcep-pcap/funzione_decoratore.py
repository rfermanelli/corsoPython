def funzione_decoratore(funzione_parametro):
    def wrapper():
        """ nome convenzionale - wrapper significa 'incarto, confezione' """
        print("... codice da eseguire prima di 'funzione_parametro' ...")
        funzione_parametro()
        print("... codice da eseguire dopo di 'funzione_parametro' ...")
    return wrapper

#def mia_funzione():
#    print("Hello World!")

# primo modo di invocazione
@funzione_decoratore
def mia_funzione():
    print("Hello World!")
mia_funzione()

# secondo modo di invocazione
mia_funzione = funzione_decoratore(mia_funzione)
mia_funzione()



