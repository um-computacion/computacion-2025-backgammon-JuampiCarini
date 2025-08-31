class Jugador:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def obtener_color(self):
        return self.color
   
    def obtener_nombre(self):
        return self.nombre
