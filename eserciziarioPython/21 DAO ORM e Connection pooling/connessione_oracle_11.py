
import oracledb


try:
    connessione_oracle = oracledb.connect(user = "utente_db",
                                      password = "utente_db",
                                      dsn = "127.0.0.1/xe")

    connessione_oracle.close()

except oracledb.Error as errore_oracle:
    print(errore_oracle)








