import getpass

import oracledb

utente = 'utente_db'
istanza = 'localhost/xe'
psw = getpass.getpass('Inserisci la password per {utente}@{istanza}: ')

with oracledb.connect(user = utente, password = psw, dsn = istanza) as connessione_oracle:
    with connessione_oracle.cursor() as cursore_oracle:
        sql = 'select ID, NOME from TEST'
        for tupla in cursore_oracle.execute(sql):
            print(tupla)
