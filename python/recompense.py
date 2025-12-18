class Recompense:
    def __init__(self, nom: str, bonusXp: int):
        self._nom = nom
        self._bonusXp = bonusXp
        self._quete = None

    def getNom(self) -> str:
        return self._nom

    def getBonusXp(self) -> int:
        return self._bonusXp

    def getQuete(self):
        return self._quete

    def setQueteInternal(self, q) -> None:
        self._quete = q