from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python.magicien import Magicien

@dataclass
class LivreMagique:
    titre: str  
    puissance_magique_livre: int 
    possesseur: Optional['Magicien'] = field(default=None, init=False)

    @property
    def points_de_magie(self) -> int:
        return self.puissance_magique_livre

    def enchanter(self):
        self.puissance_magique_livre += 10

    def deteriorer(self, amount: int):
        self.puissance_magique_livre = max(0, self.puissance_magique_livre - amount)