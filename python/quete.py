class Quete:
    def __init__(self, titre: str):
        self._titre = titre
        self._xp = 0

        self._recompense = None  

        self._joueur = None 
        
    # ---------- Getters / Setters ----------
    def getTitre(self) -> str:
        return self._titre

    def setTitre(self, titre: str) -> None:
        self._titre = titre

    def getXp(self) -> int:
        return self._xp
    
    def ajouterXp(self, xp_gagnes: int) -> None:
        if xp_gagnes > 0:
            self._xp += xp_gagnes


    # ---------- Recompense (bidirectionnel) ----------
    def getRecompense(self):
        return self._recompense

    def xpTotalAvecBonus(self) -> int:
        return self._xp if self._recompense is None else self._xp + self._recompense.getBonusXp()

    def attribuerRecompense(self, nouvelle) -> None:
        if self._recompense is nouvelle:
            return

        self._detacherRecompense()
        self._attacherRecompense(nouvelle)

    def _detacherRecompense(self) -> None:
        if self._recompense is not None:
            ancienne = self._recompense
            self._recompense = None
            ancienne.setQueteInternal(None)


    def _attacherRecompense(self, nouvelle) -> None:
        self._recompense = nouvelle
        if nouvelle is not None:
            ancienne_quete = nouvelle.getQuete()
            if ancienne_quete is not None and ancienne_quete is not self:
                ancienne_quete.attribuerRecompense(None)
            nouvelle.setQueteInternal(self)

    # ---------- Joueur (0..1) <-> (*) (bidirectionnel) ----------
    def getJoueur(self):
        return self._joueur

    def attribuerJoueur(self, nouveau) -> None:
        if self._joueur is nouveau:
            return

        # 1) Détacher de l'ancien joueur
        if self._joueur is not None:
            ancien = self._joueur
            self._joueur = None
            ancien._retirerQueteInternal(self)

        # 2) Attacher au nouveau joueur
        self._joueur = nouveau
        if nouveau is not None:
            nouveau._ajouterQueteInternal(self)

    # Méthode interne: utilisée par Joueur pour éviter boucles infinies
    def setJoueurInternal(self, j) -> None:
        self._joueur = j