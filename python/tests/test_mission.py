import unittest
from magicien import Magicien
from quete import Quete
from recompense import Recompense
from mission import Mission


class TestMission(unittest.TestCase):

    def setUp(self):
        self.magicien = Magicien("Harry")
        self.magicien.puissance = 10

        self.quete = Quete("Sauver le village")
        self.quete.ajouter_xp(20)

        self.mission = Mission(self.magicien, self.quete)

    def test_terminer_mission_ajoute_xp_sans_bonus(self):
        # Act
        self.mission.terminer()

        # Assert
        self.assertEqual(self.magicien.puissance, 30)

    def test_terminer_mission_ajoute_xp_avec_bonus(self):
        # Arrange
        recompense = Recompense("Medaille", 5)
        self.quete.attribuer_recompense(recompense)

        # Act
        self.mission.terminer()

        # Assert
        self.assertEqual(self.magicien.puissance, 35)

    def test_terminer_mission_sans_xp_ne_change_pas_puissance(self):
        # Arrange
        self.magicien.puissance = 10
        self.quete = Quete("Explorer la grotte")
        self.quete.ajouter_xp(0)
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
