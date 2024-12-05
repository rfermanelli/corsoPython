import getpass

import oracledb

try:
    connessione_oracle = oracledb.connect(user = "utente_db",
                                      password = "utente_db",
                                      dsn = "localhost/xe")

    cursore_oracle = connessione_oracle.cursor()

    query = cursore_oracle.execute('select ID, UTENTE, PASSWORD from UTENTE where ID = 1' )

    for tupla in query:
        print(tupla)

    cursore_oracle.close()
    connessione_oracle.close()

except oracledb.Error as errore_oracle:
    print(errore_oracle)





