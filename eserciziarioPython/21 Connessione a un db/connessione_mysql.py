"""
Puntare la cartella degli script dell'ambiente virtuale di pyCharmC: venv\\Scripts
Eseguire il comando: pip install mysql-connector-python
"""

import mysql.connector

cnx = mysql.connector.connect(user = 'root',
                              password = 'root',
                              host = 'localhost',
                              database = 'db_corso_python')
