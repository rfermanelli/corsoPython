import getpass

import oracledb

try:
    connessione_oracle = oracledb.connect(user = "utente_db",
                                      password = "utente_db",
                                      dsn = "localhost/xe")

    cursore_oracle = connessione_oracle.cursor()

    query = 'insert into UTENTE(ID, UTENTE, PASSWORD) values (:id, :utente, :password)'

    cursore_oracle.execute(query, [1, 'User_1', 'User_1'])

    connessione_oracle.commit()
    cursore_oracle.close()
    connessione_oracle.close()

except oracledb.Error as errore_oracle:
    print(errore_oracle)











