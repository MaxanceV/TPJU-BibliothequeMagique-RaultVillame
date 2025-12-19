import unittest
from quete import Quete
from recompense import Recompense


class TestRecompense(unittest.TestCase):

    def setUp(self):
        self.quete = Quete("Vaincre le dragon")
        self.recompense = Recompense("Épée légendaire", 100)

    def test_nom(self):
        self.assertEqual("Épée légendaire", self.recompense.nom)

    def test_bonus_xp(self):
        self.assertEqual(100, self.recompense.bonus_xp)

    def test_quete_initialement_none(self):
        self.assertIsNone(self.recompense.quete)

    def test_lier_recompense_a_quete(self):
        self.quete.attribuer_recompense(self.recompense)
        self.assertEqual(self.quete, self.recompense.quete)

    def test_delier_recompense_de_quete(self):
        self.quete.attribuer_recompense(self.recompense)
        self.quete.attribuer_recompense(None)
        self.assertIsNone(self.recompense.quete)


if __name__ == "__main__":
    unittest.main()
