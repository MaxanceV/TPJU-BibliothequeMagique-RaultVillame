import unittest
from magicien import Magicien
from livre_magique import LivreMagique

class TestMagicienComplet(unittest.TestCase):

    def setUp(self):
        # Arrange commun
        self.harry = Magicien("Harry")
        self.voldemort = Magicien("Voldemort")
        self.grimoire1 = LivreMagique("Grimoire de Poudlard", 50)
        self.grimoire2 = LivreMagique("Petit Grimoire", 20)

    def test_logique_globale_association(self):    
        # 1. Test du cumul de puissance
        self.harry.prendre_livre(self.grimoire1)
        self.harry.prendre_livre(self.grimoire2)
        self.assertEqual(self.harry.calculer_puissance_totale(), 80) # 10+50+20
        self.assertEqual(len(self.harry.livres), 2)

        # 2. Test de la bidirectionnalité
        self.assertEqual(self.grimoire1.possesseur, self.harry)

        # 3. Test du transfert de propriété (le vol de livre)
        # Voldemort essaie de prendre le grimoire1 à Harry
        self.voldemort.prendre_livre(self.grimoire1)
        
        # Assertions de transfert
        self.assertIn(self.grimoire1, self.voldemort.livres)
        self.assertEqual(self.grimoire1.possesseur, self.voldemort)
        # Harry doit l'avoir perdu
        self.assertNotIn(self.grimoire1, self.harry.livres)
        self.assertEqual(self.harry.calculer_puissance_totale(), 30) # 10+20 (livre2 restant)

    def tearDown(self):
        # Nettoyage
        self.harry.livres.clear()
        self.voldemort.livres.clear()