from magicien import Magicien
from livre_magique_de_feu import LivreMagiqueDeFeu

class MagicienDeFeu(Magicien):
    def creer_livre(self, titre: str):
        return LivreMagiqueDeFeu(titre, 15)
