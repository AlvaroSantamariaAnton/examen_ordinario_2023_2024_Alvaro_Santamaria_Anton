from EstrellaDeLaMuerte import EstrellaDeLaMuerte   # Importar clase necesaria
from Naves import NavePequena, NaveGrande           # Importar clases de Naves.py

# Crear instancias de la Estrella de la Muerte y naves aliadas
estrella_muerte = EstrellaDeLaMuerte()
nave_pequena = NavePequena("Nave Pequeña 1", 200)
nave_grande = NaveGrande("Nave Grande 1", 500)

# Atacar naves aliadas
estrella_muerte.destruir_nave(nave_pequena)
estrella_muerte.destruir_nave(nave_grande)
