class Mission:
    def __init__(self, magicien, quete):
        self.magicien = magicien
        self.quete = quete

    def terminer(self) -> None:
        xp = self.quete.xpTotalAvecBonus()
        self.magicien.ajouter_puissance(xp)
