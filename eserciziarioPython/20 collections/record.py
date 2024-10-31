automobile = {
    'marca': 'Fiat',
    'tipo': 'Panda'
}
#
automobile = ('Fiat', 'Panda')
#
class Automobile:
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo
#
from dataclasses import dataclass
@dataclass
class Automobile:
    marca: 'Fiat'
    tipo: 'Panda'

