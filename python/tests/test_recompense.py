import unittest

from Classe.Quete import Quete
from Classe.Recompense import Recompense


class TestRecompense(unittest.TestCase):

    def setUp(self):
        self.quete = Quete("Vaincre le dragon")
        self.recompense = Recompense("Épée légendaire", 100)

    def test_getNom(self):
        self.assertEqual("Épée légendaire", self.recompense.getNom())

    def test_getBonusXp(self):
        self.assertEqual(100, self.recompense.getBonusXp())

    def test_getQuete_initialementNone(self):
        self.assertIsNone(self.recompense.getQuete())

    def test_lierRecompenseAQuete(self):
        self.quete.attribuerRecompense(self.recompense)
        self.assertEqual(self.quete, self.recompense.getQuete())

    def test_delierRecompenseDeQuete(self):
        self.quete.attribuerRecompense(self.recompense)
        self.quete.attribuerRecompense(None)
        self.assertIsNone(self.recompense.getQuete())


if __name__ == "__main__":
    unittest.main()
