from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python.magicien import Magicien

@dataclass
class LivreMagique:
    titre: str  
    magie_actuelle: int 
    possesseur: Optional['Magicien'] = field(default=None, init=False)

    @property
    def points_de_magie(self) -> int:
        return self.magie_actuelle

    def enchanter(self):
        self.magie_actuelle += 10