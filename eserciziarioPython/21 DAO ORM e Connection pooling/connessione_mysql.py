"""
Puntare la cartella degli script dell'ambiente virtuale di pyCharmC: venv\\Scripts
Eseguire il comando: pip install mysql-connector-python
"""

import mysql.connector

try:
    connessione_mysql = mysql.connector.connect(user = 'root',
                                            password = 'root',
                                            host = 'localhost',
                                            database = 'db_corso_python')

    cursore_mysql = connessione_mysql.cursor()
    query = 'select ID, nome from test'
    cursore_mysql.execute(query)

except mysql.connector.Error as errore_mysql:
    print(errore_mysql)