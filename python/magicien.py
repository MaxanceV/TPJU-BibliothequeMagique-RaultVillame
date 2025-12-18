from dataclasses import dataclass, field
from typing import List
from livre_magique import LivreMagique

@dataclass
class Magicien:
    nom: str
    livres: List[LivreMagique] = field(default_factory=list, init=False)
    puissance : int = field(default=10)  # Puissance de base

    def prendre_livre(self, nouveau_livre: LivreMagique):
        if nouveau_livre not in self.livres:
            # Si le livre appartenait à quelqu'un d'autre, il doit le lâcher
            if nouveau_livre.possesseur:
                nouveau_livre.possesseur.perdre_livre(nouveau_livre)
            
            self.livres.append(nouveau_livre)
            nouveau_livre.possesseur = self

    def perdre_livre(self, livre: LivreMagique):
        if livre in self.livres:
            self.livres.remove(livre)
            livre.possesseur = None

    def obtenir_somme_magie_livres(self) -> int:
        return sum(l.points_de_magie for l in self.livres)

    def calculer_puissance_totale(self) -> int:
        return self.puissance + self.somme_point_de_magie()

    def somme_point_de_magie(self):
        somme_magie_livre = sum(l.points_de_magie for l in self.livres)
        return somme_magie_livre
    
    def ajouter_puissance(self, amount: int) -> None:
        if amount > 0:
            self.puissance += amount

    # Factory Method (peut être redéfinie)
    def creer_livre(self, titre: str) -> LivreMagique:
        return LivreMagique(titre, 10)

    def invoquer_livre(self, titre: str) -> LivreMagique:
        livre = self.creer_livre(titre)
        self.prendre_livre(livre)
        return livre
