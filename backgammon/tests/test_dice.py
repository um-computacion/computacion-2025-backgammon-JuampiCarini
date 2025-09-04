import unittest
from backgammon.core.dice import Dice

class TestDice(unittest.TestCase):
    def setUp(self):
        self.dados = Dice()

    def test_tirada_devuelve_lista(self):
        resultado = self.dados.tirar()
        self.assertIsInstance(resultado, list)

    def test_valores_siempre_entre_1_y_6(self):
        for _ in range(50):  # tiramos varias veces para estar seguros
            resultado = self.dados.tirar()
            for valor in resultado:
                self.assertTrue(1 <= valor <= 6)

    def test_doble_devuelve_cuatro_valores(self):
        # Fuerzo a simular un doble
        while True:
            resultado = self.dados.tirar()
            if len(resultado) == 4:
                self.assertEqual(len(set(resultado)), 1)  # todos iguales
                break

if __name__ == "__main__":
    unittest.main()
