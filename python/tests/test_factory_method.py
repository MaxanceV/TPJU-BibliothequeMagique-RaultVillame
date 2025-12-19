import unittest

from magicien import Magicien
from magicien_de_feu import MagicienDeFeu
from livre_magique import LivreMagique
from livre_magique_de_feu import LivreMagiqueDeFeu


class TestFactoryMethodLivre(unittest.TestCase):

    def setUp(self):
        self.magicien = Magicien("Gandalf")
        self.magicien_de_feu = MagicienDeFeu("Azar")

    def test_invoquer_livre_cree_un_livre_classique_et_l_attribue(self):
        # Arrange
        titre = "Grimoire Classique"

        # Act
        livre = self.magicien.invoquer_livre(titre)

        # Assert
        self.assertIsInstance(livre, LivreMagique)
        self.assertNotIsInstance(livre, LivreMagiqueDeFeu)
        self.assertEqual(livre.titre, titre)
        self.assertEqual(livre.possesseur, self.magicien)
        self.assertIn(livre, self.magicien.livres)

    def test_magicien_de_feu_invoquer_livre_cree_un_livre_de_feu(self):
        # Arrange
        titre = "Grimoire Incandescent"

        # Act
        livre = self.magicien_de_feu.invoquer_livre(titre)

        # Assert
        self.assertIsInstance(livre, LivreMagiqueDeFeu)
        self.assertEqual(livre.titre, titre)
        self.assertEqual(livre.possesseur, self.magicien_de_feu)
        self.assertIn(livre, self.magicien_de_feu.livres)

    def tearDown(self):
        self.magicien = None
        self.magicien_de_feu = None


if __name__ == '__main__':
    unittest.main()
