from dataclasses import dataclass, field
from typing import List
from livre_magique import LivreMagique

@dataclass
class Magicien:
    nom: str
    # Maintenant c'est une liste de livres
    livres: List[LivreMagique] = field(default_factory=list, init=False)

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
        puissance_base = 10
        return puissance_base + self.somme_point_de_magie()

    def somme_point_de_magie(self):
        somme_magie_livre = sum(l.points_de_magie for l in self.livres)
        return somme_magie_livre