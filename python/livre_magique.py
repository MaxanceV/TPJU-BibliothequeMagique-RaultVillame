from dataclasses import dataclass

@dataclass
class LivreMagique:
    titre: str  
    magie_actuelle: int 

    @property
    def points_de_magie(self) -> int:
        return self.magie_actuelle

    def enchanter(self):
        self.magie_actuelle += 10