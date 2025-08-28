class Checker:
    """
    Clase que representa una ficha de Backgammon.
    Cada ficha tiene un color (blanco o negro).
    """

    def __init__(self, color: str):
        """
        Crea una ficha con un color específico.
        
        Parámetros:
            color (str): Color de la ficha ("blanco" o "negro").
        """
        self.__color__ = color

    def obtener_color(self) -> str:
        """
        Devuelve el color de la ficha.
        """
        return self.__color__
