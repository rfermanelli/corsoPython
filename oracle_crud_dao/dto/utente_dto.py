from dataclasses import dataclass


@dataclass
class UtenteDTO:
    id_user: int
    user: str
    psw: str
