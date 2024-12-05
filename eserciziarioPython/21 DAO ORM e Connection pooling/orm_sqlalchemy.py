from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Connessione a Oracle (modifica con le tue credenziali)
engine = create_engine('oracledb://utente_db:utente_dbd@localhost:1521/xe')

# Definisci la base per le classi
Base = declarative_base()

# Definisci un modello (classe) per la tabella
class Utente(Base):
    __tablename__ = 'utenti'
    id_utente = Column(Integer, primary_key=True)
    nome_utente = Column(String)

# Crea le tabelle
Base.metadata.create_all(engine)






