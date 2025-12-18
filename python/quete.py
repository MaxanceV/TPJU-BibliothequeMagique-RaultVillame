class Quete:
    def __init__(self, titre: str):
        self.titre = titre
        self.xp = 0
        self.recompense = None  

    # ---------- Getters / Setters ----------
    def getTitre(self) -> str:
        return self.titre

    def setTitre(self, titre: str) -> None:
        self.titre = titre

    def getXp(self) -> int:
        return self.xp
    
    def ajouterXp(self, xp_gagnes: int) -> None:
        if xp_gagnes > 0:
            self.xp += xp_gagnes


    # ---------- Recompense (bidirectionnel) ----------
    def getRecompense(self):
        return self.recompense

    def xpTotalAvecBonus(self) -> int:
        return self.xp if self.recompense is None else self.xp + self.recompense.getBonusXp()

    def attribuerRecompense(self, nouvelle) -> None:
        if self.recompense is nouvelle:
            return

        self.detacherRecompense()
        self.attacherRecompense(nouvelle)

    def detacherRecompense(self) -> None:
        if self.recompense is not None:
            ancienne = self.recompense
            self.recompense = None
            ancienne.setQueteInternal(None)


    def attacherRecompense(self, nouvelle) -> None:
        self.recompense = nouvelle
        if nouvelle is not None:
            ancienne_quete = nouvelle.getQuete()
            if ancienne_quete is not None and ancienne_quete is not self:
                ancienne_quete.attribuerRecompense(None)
            nouvelle.setQueteInternal(self)
