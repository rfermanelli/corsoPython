import getpass

import oracledb

connessione_oracle = oracledb.connect(user = "utente_db",
                                      password = "utente_db",
                                      dsn = "localhost/xe")

cursore_oracle = connessione_oracle.cursor()

for tupla in cursore_oracle.execute('select ID, NOME from TEST'):
    if (tupla[1]):
        print('ID =', tupla[0], '; ' 'NOME =', tupla[1])
