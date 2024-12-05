import oracledb

from oracle_crud_dao.utility.db_connection import get_connection
from oracle_crud_dao.dto.utente_dto import UtenteDTO


class UtenteDAO:
    @staticmethod
    def insert_utente(utente: UtenteDTO):
        try:
            connessione = get_connection()
            cursore = connessione.cursor()
            query = """INSERT INTO UTENTE (ID_UTENTE, UTENTE, PSW) 
                    VALUES (:id_utente, :utente, :psw)"""
            cursore.execute(query, [utente.id_user, utente.user, utente.psw])
            connessione.commit()
            cursore.close()
            connessione.close()
            return 0
        except oracledb.Error as db_error:
            return db_error

    @staticmethod
    def read_utente(id_user: int) -> UtenteDTO:
        try:
            connessione = get_connection()
            cursore = connessione.cursor()
            query = """ SELECT ID_UTENTE, UTENTE, PSW
                        FROM UTENTE 
                        WHERE ID_UTENTE = :id_user"""
            cursore.execute(query, [id_user])
            tupla = cursore.fetchone()
            connessione.commit()
            cursore.close()
            connessione.close()
            if tupla:
                # Il metodo fetchone() estrae la tupla successiva di un insieme di tuple
                return UtenteDTO(id_user=tupla[0], user=tupla[1], psw=tupla[2])
            return UtenteDTO(id_user=0, user='', psw='')
        except oracledb.Error as db_error:
            print('Errore generato dal livello DAO: ', db_error)

    @staticmethod
    def update_utente(utente: UtenteDTO):
        try:
            connessione = get_connection()
            cursore = connessione.cursor()
            query = """UPDATE UTENTE 
                       SET 
                            UTENTE = :username,
                            PSW = :psw
                        WHERE
                            ID_UTENTE = :id_user"""
            bind_values = {
                'username': utente.user,
                'psw': utente.psw,
                'id_user': utente.id_user
            }
            cursore.execute(query, bind_values)
            connessione.commit()
            cursore.close()
            connessione.close()
            return 0
        except oracledb.Error as db_error:
            return db_error

    @staticmethod
    def delete_utente(id_user: int):
        try:
            connessione = get_connection()
            cursore = connessione.cursor()
            query = """DELETE FROM UTENTE 
                       WHERE
                            ID_UTENTE = :id_user"""
            cursore.execute(query, [id_user])
            connessione.commit()
            cursore.close()
            connessione.close()
            return 0
        except oracledb.Error as db_error:
            return db_error

    @staticmethod
    def read_all():
        try:
            connessione = get_connection()
            cursore = connessione.cursor()
            query = """SELECT
                            ID_UTENTE,
                            UTENTE,
                            PSW
                        FROM
                            UTENTE"""
            cursore.execute(query)
            tuple = cursore.fetchall()
            connessione.commit()
            cursore.close()
            connessione.close()
            if tuple:
                # Il metodo fetchall() estrae le tuple rimanenti di un insieme di tuple
                #utenti = [UtenteDTO(id_user=tupla[0], user=tupla[1], psw=tupla[2]) for tupla in tuple]
                utenti = [(tupla[0], tupla[1], tupla[2]) for tupla in tuple]
                return utenti
        except oracledb.Error as db_error:
            return db_error