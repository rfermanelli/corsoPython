def display_a_tredici_led(numero):
    indice_di_stampa = [0,0,0,0,0,0,0,0,0,0]
    def zero():

        zero = [['#','#','#'], ['#',' ','#'], ['#',' ','#'], ['#',' ','#'], ['#','#','#']]
        indice_di_stampa[0] = 1
    def uno():
        uno_s =  [[' ',' ','#'], [' ',' ','#'], [' ',' ','#'], [' ',' ','#'], [' ',' ','#']]
        global uno

        indice_di_stampa[1] = 1
    def due():
        due = [['#', '#', '#'], [' ', ' ', '#'], ['#', '#', '#'], ['#', ' ', ' '], ['#', '#', '#']]
        indice_di_stampa[2] = 1
    def tre():
        tre = [['#', '#', '#'], [' ', ' ', '#'], ['#', '#', '#'], [' ', ' ', '#'], ['#', '#', '#']]
        indice_di_stampa[3] = 1
    def quattro():
        quattro = [['#', ' ', '#'], ['#', ' ', '#'], ['#', '#', '#'], [' ', ' ', '#'], [' ', ' ', '#']]
        indice_di_stampa[4] = 1
    def cinque():
        cinque = [['#', '#', '#'], ['#', ' ', ' '], ['#', '#', '#'], [' ', ' ', '#'], ['#', '#', '#']]
        indice_di_stampa[5] = 1
    def sei():
        sei = [['#', '#', '#'], ['#', ' ', ' '], ['#', '#', '#'], ['#', ' ', '#'], ['#', '#', '#']]
        indice_di_stampa[6] = 1
    def sette():
        sette = [['#', '#', '#'], [' ', ' ', '#'], [' ', ' ', '#'], [' ', ' ', '#'], [' ', ' ', '#']]
        indice_di_stampa[7] = 1
    def otto():
        otto = [['#', '#', '#'], ['#', ' ', '#'], ['#', '#', '#'], ['#', ' ', '#'], ['# ', '#', '#']]
        indice_di_stampa[8] = 1
    def nove():
        nove = [['#', '#', '#'], ['#', ' ', '#'], ['#', '#', '#'], [' ', ' ', '#'], ['#', '#', '#']]
        indice_di_stampa[9] = 1
    def display():
        for indice in indice_di_stampa:
            print(uno_s, otto)
    d = {0:zero(), 1:uno(), 2:due(), 3:tre(), 4:quattro(), 5:cinque(), 6:sei(), 7:sette(), 8:otto(), 9:nove()}
    if numero.isdigit():
        numero_da_visualizzare = list(numero)
        for cifra in numero_da_visualizzare:
            d[int(cifra)]
            display()

display_a_tredici_led('18')