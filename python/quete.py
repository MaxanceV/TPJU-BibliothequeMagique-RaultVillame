from __future__ import annotations
from typing import Optional
from recompense import Recompense


class Quete:
    def __init__(self, titre: str):
        self.titre = titre
        self.xp = 0
        self.recompense: Optional[Recompense] = None

    def ajouter_xp(self, xp_gagnes: int) -> None:
        if xp_gagnes > 0:
            self.xp += xp_gagnes

    def xp_total_avec_bonus(self) -> int:
        return self.xp if self.recompense is None else self.xp + self.recompense.bonus_xp

    def attribuer_recompense(self, nouvelle: Optional[Recompense]) -> None:
        if self.recompense is nouvelle:
            return
        self.detacher_recompense()
        self.attacher_recompense(nouvelle)

    def detacher_recompense(self) -> None:
        if self.recompense is not None:
            ancienne = self.recompense
            self.recompense = None
            ancienne.set_quete_internal(None)

    def attacher_recompense(self, nouvelle: Optional[Recompense]) -> None:
        self.recompense = nouvelle
        if nouvelle is not None:
            ancienne_quete = nouvelle.quete
            if ancienne_quete is not None and ancienne_quete is not self:
                ancienne_quete.attribuer_recompense(None)
            nouvelle.set_quete_internal(self)
