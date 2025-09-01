from backgammon.core.player import Jugador
from backgammon.core.checker import Checker

class Tablero:
    """
    Tablero de Backgammon con 24 casillas y barra de fichas capturadas.
    """

    def __init__(self):
        self.__casillas__ = [[] for _ in range(24)]
        self.__capturadas__ = {"blanco": [], "negro": []}
        self._inicializar()

    def _inicializar(self):
        """Posición inicial estándar."""
        self.__casillas__ = [[] for _ in range(24)]

        # Blanco
        self.__casillas__[23] = [Checker("blanco") for _ in range(2)]
        self.__casillas__[12] = [Checker("blanco") for _ in range(5)]
        self.__casillas__[7]  = [Checker("blanco") for _ in range(3)]
        self.__casillas__[5]  = [Checker("blanco") for _ in range(5)]

        # Negro
        self.__casillas__[0]  = [Checker("negro") for _ in range(2)]
        self.__casillas__[11] = [Checker("negro") for _ in range(5)]
        self.__casillas__[16] = [Checker("negro") for _ in range(3)]
        self.__casillas__[18] = [Checker("negro") for _ in range(5)]

        self.__capturadas__ = {"blanco": [], "negro": []}

    def poner_ficha(self, color: str, pos: int):
        self.__casillas__[pos].append(Checker(color))

    def sacar_ficha(self, pos: int) -> bool:
        if not self.__casillas__[pos]:
            return False
        self.__casillas__[pos].pop()
        return True

    def enviar_a_barra(self, color: str):
        self.__capturadas__[color].append(Checker(color))

    def sacar_de_barra(self, color: str) -> bool:
        if not self.__capturadas__[color]:
            return False
        self.__capturadas__[color].pop()
        return True

    def ver_casillas(self):
        return self.__casillas__

    def ver_barra(self):
        return self.__capturadas__
