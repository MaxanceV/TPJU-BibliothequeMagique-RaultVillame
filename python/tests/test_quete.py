import unittest

from Classe.Quete import Quete
from Classe.Recompense import Recompense


class TestQuete(unittest.TestCase):

    def setUp(self):
        self.quete = Quete("Sauver le village")
        self.recompense = Recompense("Sac d’or", 20)
        self.quete.attribuerRecompense(self.recompense)

    def test_ajouterXp_augmenteXp(self):
        self.quete.ajouterXp(10)
        self.assertEqual(10, self.quete.getXp())

    def test_xpTotalAvecBonus_utiliseRecompense(self):
        self.quete.ajouterXp(10)
        self.assertEqual(30, self.quete.xpTotalAvecBonus())

    def test_ajouterXp_ignoreValeursInvalides(self):
        self.quete.ajouterXp(-5)
        self.quete.ajouterXp(0)
        self.assertEqual(0, self.quete.getXp())

    def test_uneRecompenseNePeutAvoirQuUneQuete(self):
        q1 = Quete("Q1")
        q2 = Quete("Q2")
        r = Recompense("Couronne", 50)

        q1.attribuerRecompense(r)
        q2.attribuerRecompense(r)

        self.assertIsNone(q1.getRecompense())
        self.assertEqual(r, q2.getRecompense())
        self.assertEqual(q2, r.getQuete())


if __name__ == "__main__":
    unittest.main()
