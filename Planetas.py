# Creamos la clase padre Planetas
class Planeta:
    
    # Definimos el constructor con las propiedades
    def __init__(self, nombre, volumen, clasificacion):
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion

# Creamos la clase Concordia heredada de Planeta
class Concordia(Planeta):
    
    # Definimos el constructor que hereda las propiedades de la clase padre
    def __init__(self, nombre):
        super().__init__(nombre, 500, 1)


# Creamos la clase Ilum heredada de Planeta
class Ilum(Planeta):
    
    # Definimos el constructor que hereda las propiedades de la clase padre
    def __init__(self, nombre):
        super().__init__(nombre, 1200, 2)


# Creamos la clase Kamino heredada de Planeta
class Kamino(Planeta):
    
    # Definimos el constructor que hereda las propiedades de la clase padre
    def __init__(self, nombre):
        super().__init__(nombre, 800, 3)