class Planeta:
    
    def __init__(self, nombre, volumen, clasificacion):
        
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion
        
class Concordia(Planeta):
    def __init__(self, nombre, volumen, clasificacion):
        super().__init__(nombre, volumen, clasificacion)
        

class Ilum(Planeta):
    def __init__(self, nombre, volumen, clasificacion):
        super().__init__(nombre, volumen, clasificacion)
        

class Kamino(Planeta):
    def __init__(self, nombre, volumen, clasificacion):
        super().__init__(nombre, volumen, clasificacion)