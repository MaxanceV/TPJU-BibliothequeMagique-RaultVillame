import unittest
from quete import Quete
from recompense import Recompense


class TestQuete(unittest.TestCase):

    def setUp(self):
        self.quete = Quete("Sauver le village")
        self.recompense = Recompense("Sac d’or", 20)
        self.quete.attribuer_recompense(self.recompense)

    def test_ajouter_xp_augmente_xp(self):
        # Arrange (reset à 0 car setUp n'ajoute pas d'xp)
        # Act
        self.quete.ajouter_xp(10)

        # Assert
        self.assertEqual(10, self.quete.xp)

    def test_xp_total_avec_bonus_utilise_recompense(self):
        # Act
        self.quete.ajouter_xp(10)

        # Assert (10 + bonus 20)
        self.assertEqual(30, self.quete.xp_total_avec_bonus())

    def test_ajouter_xp_ignore_valeurs_invalides(self):
        # Act
        self.quete.ajouter_xp(-5)
        self.quete.ajouter_xp(0)

        # Assert
        self.assertEqual(0, self.quete.xp)

    def test_une_recompense_ne_peut_avoir_qu_une_quete(self):
        # Arrange
        q1 = Quete("Q1")
        q2 = Quete("Q2")
        r = Recompense("Couronne", 50)

        # Act
        q1.attribuer_recompense(r)
        q2.attribuer_recompense(r)

        # Assert
        self.assertIsNone(q1.recompense)
        self.assertEqual(r, q2.recompense)
        self.assertEqual(q2, r.quete)


if __name__ == "__main__":
    unittest.main()
