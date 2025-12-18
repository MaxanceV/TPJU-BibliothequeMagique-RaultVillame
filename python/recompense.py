class Recompense:
    def __init__(self, nom: str, bonusXp: int):
        self.nom = nom
        self.bonusXP = bonusXp
        self.quete = None

    def getNom(self) -> str:
        return self.nom

    def getBonusXp(self) -> int:
        return self.bonusXP

    def getQuete(self):
        return self.quete

    def setQueteInternal(self, q) -> None:
        self.quete = q