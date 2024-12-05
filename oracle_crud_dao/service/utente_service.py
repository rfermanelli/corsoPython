from oracle_crud_dao.dao.utente_dao import UtenteDAO
from oracle_crud_dao.dto.utente_dto import UtenteDTO


class UtenteService:
    @staticmethod
    def insert_utente(id_user: int, user: str, psw: str):
        utente_dto = UtenteDTO(id_user=id_user, user=user, psw=psw)
        return UtenteDAO.insert_utente(utente_dto)

    @staticmethod
    def read_utente(id_user: int) -> UtenteDTO:
        return UtenteDAO.read_utente(id_user)

    @staticmethod
    def update_utente(id_user: int, user: str, psw: str):
        utente_dto = UtenteDTO(id_user=id_user, user=user, psw=psw)
        return UtenteDAO.update_utente(utente_dto)

    @staticmethod
    def delete_utente(id_user: int) -> UtenteDTO:
        return UtenteDAO.delete_utente(id_user)

    @staticmethod
    def read_all():
        return UtenteDAO.read_all()
