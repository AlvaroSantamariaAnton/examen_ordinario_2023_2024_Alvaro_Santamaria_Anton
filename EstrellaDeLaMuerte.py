from Planetas import Concordia, Ilum, Kamino    # Importamos las clases necesarias de Planetas.py

# Creamos la clase EstrellaDeLaMuerte
class EstrellaDeLaMuerte:
    
    # Definimos el constructor y sus propiedades
    def __init__(self):
        
        self.puntos_vida = 1000

    # Definimos el método destruir_planeta
    def destruir_planeta(self, planeta):
        
        if planeta.volumen <= self.puntos_vida:
            print(f"\nLa Estrella de la Muerte ha destruido el planeta {planeta.nombre}.")
            self.puntos_vida = self.puntos_vida - planeta.volumen
            print(f"La Estrella de la Muerte ha perdido {planeta.volumen} puntos de vida. Vida actual: {self.puntos_vida}")
        else:
            print(f"\nNo se puede destruir el planeta {planeta.nombre}. Puntos de vida insuficientes.")
    
    # Definimos el método estado
    def estado(self):
        
        if self.puntos_vida <= 0:
            print("\nLa Estrella de la muerte ha sido destruida.")
        else:
            print(f"\nLa Estrella de la Muerte tiene {self.puntos_vida} puntos de vida")


if __name__ == "__main__":
    # Creamos las instancias de los planetas y la Estrella de la Muerte
    concordia = Concordia("Concordia")
    ilum = Ilum("Ilum")
    kamino = Kamino("Kamino")
    estrella_muerte = EstrellaDeLaMuerte()

    # Llamar al método destruir_planeta para cada planeta
    estrella_muerte.destruir_planeta(concordia)
    estrella_muerte.destruir_planeta(ilum)
    estrella_muerte.destruir_planeta(kamino)

    # Llamar al método estado para comprobar la vitalidad de la Estrella de la Muerte
    estrella_muerte.estado()