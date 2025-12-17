from dataclasses import dataclass, field
from typing import Optional
from livre_magique import LivreMagique

@dataclass
class Magicien:
    _nom: str
    _mon_livre: Optional[LivreMagique] = field(default=None, init=False)

    @property
    def nom(self) -> str:
        return self._nom

    @property
    def son_livre(self) -> Optional[LivreMagique]:
        return self._mon_livre

    def prendre_livre(self, livre: LivreMagique):
       self._mon_livre = livre

    @property
    def puissance_totale(self) -> int:
        base = 10
        if self.mon_livre:
            return base + self.mon_livre.points_de_magie
        return base