import oracledb
from oracle_crud_dao.config import configuration_file


def get_connection():
    try:
        db_connection = oracledb.connect(configuration_file.dsn)
    except oracledb.Error as db_connection_error:
        return db_connection_error

    return db_connection




