from dataclasses import dataclass, field
from typing import Optional
from livre_magique import LivreMagique

@dataclass
class Magicien:
    nom: str
    mon_livre: Optional[LivreMagique] = field(default=None, init=False)

    def prendre_livre(self, nouveau_livre: LivreMagique):
        self.mon_livre = nouveau_livre

    def calculer_puissance_totale(self) -> int:
        base = 10
        if self.mon_livre:
            return base + self.mon_livre.points_de_magie
        return base