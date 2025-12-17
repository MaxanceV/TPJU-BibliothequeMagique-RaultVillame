from dataclasses import dataclass, field
from typing import Optional

@dataclass
class LivreMagique:
    titre: str  # Attribut simple
    magie_actuelle: int  # On stocke la valeur ici

    @property
    def get_points_de_magie(self) -> int:
        return self.magie_actuelle
    
    @property
    def get_titre(self) -> str:
        return self.titre

    def enchanter(self):
        self.magie_actuelle += 10

