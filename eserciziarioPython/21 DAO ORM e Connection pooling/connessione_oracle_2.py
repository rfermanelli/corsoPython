import getpass

import oracledb

utente = 'utente_db'
istanza = 'localhost/xe'
psw = input('Inserisci la password per: ' f'{utente}@{istanza}: ')

try:
    with oracledb.connect(user = utente, password = psw, dsn = istanza) as connessione_oracle:
        with connessione_oracle.cursor() as cursore_oracle:
            sql = 'select CODP, NOMEP from PRODOTTI'
            for tupla in cursore_oracle.execute(sql):
                print(tupla)

except oracledb.Error as errore_oracle:
    print(errore_oracle)
