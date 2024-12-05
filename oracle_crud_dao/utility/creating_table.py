import oracledb
from oracle_crud_dao.utility import db_connection

def create_utente():
    try:
        db_connect = db_connection.get_connection()
        db_cursore = db_connect.cursor()
        query = """CREATE TABLE UTENTE(
            ID_UTENTE INTEGER PRIMARY KEY,
            UTENTE VARCHAR2(50) NOT NULL,
            PSW VARCHAR2(50) NOT NULL)"""
        db_cursore.execute(query)
        db_cursore.close()
        db_connect.close()
    except oracledb.Error as db_create_table_error:
        return db_create_table_error


