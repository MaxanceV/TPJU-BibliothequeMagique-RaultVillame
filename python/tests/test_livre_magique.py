import unittest
from magicien import Magicien
from livre_magique import LivreMagique


class TestLivreMagique(unittest.TestCase):

    def setUp(self):
        self.livre = LivreMagique("Livre Usé", 30)

    def test_deterioration_livre(self):
        # Act
        self.livre.deteriorer(5)

       # Assert
        self.assertEqual(self.livre.points_de_magie, 25)

    def test_deterioration_ne_devient_pas_negative(self):
       # Act
       self.livre.deteriorer(50)

       # Assert
       self.assertEqual(self.livre.points_de_magie, 0)

    def tearDown(self):
       self.livre = None

       
if __name__ == '__main__':
    unittest.main()