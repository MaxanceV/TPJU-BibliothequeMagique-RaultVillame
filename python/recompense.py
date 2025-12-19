from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from quete import Quete


@dataclass
class Recompense:
    nom: str
    bonus_xp: int
    quete: Optional["Quete"] = None

    def set_quete_internal(self, q: Optional["Quete"]) -> None:
        self.quete = q
