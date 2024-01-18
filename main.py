from EstrellaDeLaMuerte import EstrellaDeLaMuerte
from Naves import NavePequena, NaveGrande

# Crear instancias de la Estrella de la Muerte y naves aliadas
estrella_muerte = EstrellaDeLaMuerte()
nave_pequena = NavePequena("Nave Pequeña 1", 200)
nave_grande = NaveGrande("Nave Grande 1", 500)

# Atacar naves aliadas
estrella_muerte.destruir_nave(nave_pequena)
estrella_muerte.destruir_nave(nave_grande)
