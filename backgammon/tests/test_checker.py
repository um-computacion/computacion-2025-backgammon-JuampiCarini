import unittest
from backgammon.core.checker import Checker

class TestChecker(unittest.TestCase):
    def test_crear_checker(self):
        ficha = Checker("blanco")
        self.assertEqual(ficha.obtener_color(), "blanco")

if __name__ == "__main__":
    unittest.main()
