import getpass

import oracledb

try:
    connessione_oracle = oracledb.connect(user = "lutente_db",
                                      password = "utente_db",
                                      dsn = "localhost/xe")

    cursore_oracle = connessione_oracle.cursor()

    query = 'select CODP, NOMEP, COLORE, TAGLIA, MAGAZZINO from PRODOTTI'

    for tupla in cursore_oracle.execute(query):
        print(tupla)

    cursore_oracle.close()
    connessione_oracle.close()

except oracledb.Error as errore_oracle:
    print(errore_oracle)






