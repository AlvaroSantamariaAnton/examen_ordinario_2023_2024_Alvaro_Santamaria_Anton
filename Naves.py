from EstrellaDeLaMuerte import EstrellaDeLaMuerte

# Creamos clase NavePequeña heredada
class NavePequena(EstrellaDeLaMuerte):
    def __init__(self, nombre, puntos_vida):
        super().__init__()
        self.nombre = nombre
        self.puntos_vida = puntos_vida

    def recibir_ataque(self, puntos_ataque):
        if self.puntos_vida <= puntos_ataque:
            print(f"La Nave Pequeña {self.nombre} ha sido destruida.")
            self.puntos_vida = 0
        else:
            print(f"La Nave Pequeña {self.nombre} ha resistido el ataque.")
            self.puntos_vida -= puntos_ataque
            
# Creamos clase NavePequeña heredada
class NaveGrande(EstrellaDeLaMuerte):
    def __init__(self, nombre, puntos_vida):
        super().__init__()
        self.nombre = nombre
        self.puntos_vida = puntos_vida

    def recibir_ataque(self, puntos_ataque):
        if self.puntos_vida <= puntos_ataque:
            print(f"La Nave Grande {self.nombre} ha sido destruida.")
            self.puntos_vida = 0
        else:
            print(f"La Nave Grande {self.nombre} ha resistido el ataque.")
            self.puntos_vida -= puntos_ataque
