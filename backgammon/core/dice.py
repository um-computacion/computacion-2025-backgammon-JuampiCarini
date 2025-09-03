import random

class Dice:
    """
    Representa los dos dados del Backgammon.
    """

    def __init__(self):
        self.__resultados__ = []

    def tirar(self):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        if d1 == d2:
            self.__resultados__ = [d1] * 4
        else:
            self.__resultados__ = [d1, d2]

        return self.__resultados__

    def obtener_resultados(self):
        return self.__resultados__



if __name__ == "__main__":
    dados = Dice()
    print("Tirada:", dados.tirar())
