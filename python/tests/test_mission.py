import unittest
from magicien import Magicien
from quete import Quete
from recompense import Recompense
from mission import Mission


class TestMission(unittest.TestCase):

    def setUp(self):
        # Arrange (commun)
        self.magicien = Magicien("Harry")
        self.magicien.puissance = 10

        self.quete = Quete("Sauver le village")
        self.quete.ajouterXp(20)

        self.mission = Mission(self.magicien, self.quete)

    def test_terminer_mission_ajoute_xp_sans_bonus(self):
        # Act
        self.mission.terminer()

        # Assert
        self.assertEqual(self.magicien.puissance, 30)

    def test_terminer_mission_ajoute_xp_avec_bonus(self):
        # Arrange (spécifique)
        recompense = Recompense("Medaille", 5)
        self.quete.attribuerRecompense(recompense)

        # Act
        self.mission.terminer()

        # Assert
        self.assertEqual(self.magicien.puissance, 35)

    def test_terminer_mission_sans_xp_ne_change_pas_puissance(self):
        # Arrange (spécifique)
        self.magicien.puissance = 10
        self.quete = Quete("Explorer la grotte")  # nouvelle quête
        self.quete.ajouterXp(0)
        self.mission = Mission(self.magicien, self.quete)

        # Act
        self.mission.terminer()

        # Assert
        self.assertEqual(self.magicien.puissance, 10)

    def tearDown(self):
        self.magicien = None
        self.quete = None
        self.mission = None


if __name__ == '__main__':
    unittest.main()
