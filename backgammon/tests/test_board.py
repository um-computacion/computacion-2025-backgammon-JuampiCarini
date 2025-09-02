import unittest
from backgammon.core.board import Tablero

class TestTablero(unittest.TestCase):
    def test_tablero_inicia_con_24_casillas(self):
        tablero = Tablero()
        self.assertEqual(len(tablero.ver_casillas()), 24)

    def test_barra_inicia_vacia(self):
        tablero = Tablero()
        self.assertEqual(tablero.ver_barra(), {"blanco": [], "negro": []})

if __name__ == "__main__":
    unittest.main()
