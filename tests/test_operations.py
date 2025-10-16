import unittest

from calculator import calculator


class TestOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.addition(1, 2), 3)

    def test_addition_big(self):
        self.assertEqual(calculator.addition(1000, 2000), 3000)

    def test_soustraction(self):
        self.assertEqual(calculator.soustraction(2, 3), -1)
        self.assertEqual(calculator.soustraction(10, 7), 3)

    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(4, 3), 12)

    def test_division(self):
        self.assertEqual(calculator.division(10, 2), 5)

    def test_quotient(self):
        self.assertEqual(calculator.quotient(13, 2), 6)

    def test_reste(self):
        self.assertEqual(calculator.reste(23, 8), 7)

    def test_valeur_absolue(self):
        self.assertEqual(calculator.valeur_absolue(-2), 2)

    def test_carre(self):
        self.assertEqual(calculator.carre(4), 16)

    def test_racine_carre(self):
        self.assertEqual(calculator.racine_carre(16), 4)

    def test_somme_liste(self):
        self.assertEqual(calculator.somme_liste([5, 6, 7]), 18)

    def test_puissance(self):
        self.assertEqual(calculator.puissance(4, 3), 64)

    def test_inverse(self):
        self.assertEqual(calculator.inverse(5), 1 / 5)

    def test_inverse_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.inverse(0)

    def test_tri(self):
        self.assertEqual(calculator.tri([4, 2, 8]), [2, 4, 8])

    def test_tri_immutable(self):
        test_list = [4, 2, 8]
        self.assertEqual(calculator.tri(test_list), [2, 4, 8])
        self.assertEqual(test_list, [4, 2, 8])

    def test_factoriel(self):
        self.assertEqual(calculator.factoriel(4), 24)

    def test_factoriel_start(self):
        self.assertEqual(calculator.factoriel(0), 1)

    def test_maximum(self):
        self.assertEqual(calculator.maximum([1, -4, 200, 47]), 200)

    def test_logarithme(self):
        self.assertEqual(calculator.logarithme(100), 2)
