import unittest
from backgammon.core.board import Tablero

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()

    def test_tablero_inicia_con_24_casillas(self):
        self.assertEqual(len(self.tablero.ver_casillas()), 24)

    def test_barra_inicia_vacia(self):
        self.assertEqual(self.tablero.ver_barra(), {"blanco": [], "negro": []})

    def test_poner_y_sacar_ficha(self):
        # Poner ficha en la casilla 0
        self.tablero.poner_ficha("blanco", 0)
        self.assertEqual(len(self.tablero.ver_casillas()[0]), 1)

        # Sacar ficha de la casilla 0
        self.assertTrue(self.tablero.sacar_ficha(0))
        self.assertEqual(len(self.tablero.ver_casillas()[0]), 0)

    def test_sacar_ficha_de_casilla_vacia(self):
        # Intentar sacar de una casilla vacía
        self.assertFalse(self.tablero.sacar_ficha(10))

    def test_enviar_y_sacar_de_barra(self):
        # Enviar ficha a la barra
        self.tablero.enviar_a_barra("negro")
        self.assertEqual(len(self.tablero.ver_barra()["negro"]), 1)

        # Sacar ficha de la barra
        self.assertTrue(self.tablero.sacar_de_barra("negro"))
        self.assertEqual(len(self.tablero.ver_barra()["negro"]), 0)

    def test_sacar_de_barra_vacia(self):
        # Intentar sacar de barra vacía
        self.assertFalse(self.tablero.sacar_de_barra("blanco"))

if __name__ == "__main__":
    unittest.main()
    