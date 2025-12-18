from dataclasses import dataclass, field
from typing import Optional
from livre_magique import LivreMagique

@dataclass
class Magicien:
    nom: str
    livre: Optional[LivreMagique] = field(default=None, init=False)

    def prendre_livre(self, nouveau_livre: LivreMagique):
        self.livre = nouveau_livre

    @property
    def puissance_totale(self) -> int:
        base = 10
        if self.livre:
            return base + self.livre.points_de_magie
        return base