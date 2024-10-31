from dataclasses import dataclass

"""
@dataclass
class Pianeta:
    diametro_in_km: float
    massa_rispetto_terra: float
    densita_rispetto_acqua: float
    temperatura_media_superficiale_celsius: tuple
"""

class Pianeta:
    def __init__(self, diametro_in_km, massa_rispetto_terra, densita_rispetto_acqua, temperatura_media_superficiale_celsius):
        self.diametro_in_km = diametro_in_km
        self.massa_rispetto_terra = massa_rispetto_terra
        self.densita_rispetto_acqua =densita_rispetto_acqua
        self.temperatura_media_superficiale_celsius = temperatura_media_superficiale_celsius

mercurio = Pianeta(4878, 0.055, 5.43, (-180, 430))

print(mercurio.__str__())



