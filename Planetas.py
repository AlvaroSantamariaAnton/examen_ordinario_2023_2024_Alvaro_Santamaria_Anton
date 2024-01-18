class Planeta:
    
    def __init__(self, nombre, volumen, clasificacion):
        
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion
        
class Concordia(Planeta):
    def __init__(self, nombre, volumen, clasificacion):
        super().__init__(nombre, volumen, clasificacion)
        
        self.volumen = 500
        self.clasificacion = 1

class Ilum(Planeta):
    def __init__(self, nombre, volumen, clasificacion):
        super().__init__(nombre, volumen, clasificacion)
        
        self.volumen = 1200
        self.clasificacion = 2
        
class Kamino(Planeta):
    def __init__(self, nombre, volumen, clasificacion):
        super().__init__(nombre, volumen, clasificacion)
        
        self.volumen = 800
        self.clasificacion = 3
        
        
planeta_1 = Kamino(Planeta)