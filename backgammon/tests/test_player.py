import unittest
from backgammon.core.player import Jugador

class TestJugador(unittest.TestCase):
    def test_crear_jugador(self):
        jugador = Jugador("Ana", "blanco")
        self.assertEqual(jugador.obtener_nombre(), "Ana")
        self.assertEqual(jugador.obtener_color(), "blanco")

if __name__ == "__main__":
    unittest.main()
