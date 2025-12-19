class Mission:
    def __init__(self, magicien, quete):
        self.magicien = magicien
        self.quete = quete

    def terminer(self) -> None:
        xp = self.quete.xp_total_avec_bonus()
        self.magicien.ajouter_puissance(xp)
