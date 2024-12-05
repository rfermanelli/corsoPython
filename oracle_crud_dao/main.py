from oracle_crud_dao.utility import creating_table
from oracle_crud_dao.service.utente_service import UtenteService


def main():

    #db_create_table_error = creating_table.create_utente()

    #if not db_create_table_error:
    if 1:

        while True:
            print("\nMenu app:")
            print("1 ---> Inserimento utente")
            print("2 ---> Visualizzazione utente")
            print("3 ---> Aggiornamento utente")
            print("4 ---> Cancellazione utente")
            print("5 ---> Visualizzazione utenti")
            print("6 ---> Uscita")

            scelta_menu = input("Seleziona un'opzione: ")

            if scelta_menu == '1':
                print('Funzione di inserimento utente')
                id_user = int(input("Identificativo ---> "))
                user = input("User ---> ")
                psw = input("Password ---> ")
                esito_inserimento_utente = UtenteService.insert_utente(id_user, user, psw)
                if esito_inserimento_utente == 0:
                    print("---> Utente inserito")
                else:
                    print(esito_inserimento_utente)

            elif scelta_menu == '2':
                print('Funzione di visualizzazione utente')
                id_user = int(input("Identificativo --->: "))
                esito_visualizzazione_utente = UtenteService.read_utente(id_user)
                if esito_visualizzazione_utente == 0:
                    print('---> Utente inesistente')
                else:
                    print('--->', f"Id utente: {esito_visualizzazione_utente.id_user}, "
                          f"User: {esito_visualizzazione_utente.user}, "
                          f"password: {esito_visualizzazione_utente.psw}")

            elif scelta_menu == '3':
                print('Funzione di aggiornamento utente')
                id_user = int(input("Identificativo ---> "))
                user = input("User ---> ")
                psw = input("Password ---> ")
                esito_aggiornamento_utente = UtenteService.update_utente(id_user, user, psw)
                if esito_aggiornamento_utente == 0:
                    print("---> Utente aggiornato")
                else:
                    print("Aggiornamento utente fallito. codice errore: ", esito_aggiornamento_utente)

            elif scelta_menu == '4':
                print('Funzione di cancellazione utente')
                id_user = int(input("Identificativo ---> "))
                esito_cancellazione_utente = UtenteService.delete_utente(id_user)
                if esito_cancellazione_utente == 0:
                    print("---> Utente cancellato")
                else:
                    print("Cancellazione utente fallita. codice errore ---> ", esito_cancellazione_utente)


            elif scelta_menu == '5':
                print('Funzione di visualizzaizone di tutti gli utenti')
                all = input("Visualizzare la lista degli utenti? si/no ---> ")
                if all == 'si':
                    utenti = UtenteService.read_all()
                    print(utenti)

            elif scelta_menu == '6':
                print('Funzione di uscita dall\'applicazione')
                print('---> Sei uscito dal menù')
                break

            else:
                print('La scelta del menù non è valida. Riprova')
    else:
        print('Errore generato durante la creazione della tabella: ', db_create_table_error)


if __name__ == '__main__':
    main()
