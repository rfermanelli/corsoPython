def funzione_decoratore(funzione_parametro):
    def wrapper():
        """ nome convenzionale - wrapper significa 'incarto, confezione' """
        print("... codice da eseguire prima di 'funzione_parametro' ...")
        funzione_parametro()
        print("... codice da eseguire dopo di 'funzione_parametro' ...")
    return wrapper


@funzione_decoratore
def mia_funzione():
    print("Hello World!")
mia_funzione()

