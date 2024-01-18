import time

# Definir variables
tiempo_carlsen = 180  # 3 minutos
tiempo_nakamura = 180  # 3 minutos
tiempo_movimiento = 10  # tiempo inicial por movimiento en segundos

# Iniciar el juego con el turno de Magnus Carlsen
turno_actual = "Carlsen"

while True:
    # Mostrar tiempo actual y turno
    print(f"\nTiempo Carlsen: {tiempo_carlsen} segundos")
    print(f"\nTiempo Nakamura: {tiempo_nakamura} segundos")
    print(f"\nTurno de {turno_actual}")

    # Solicitar entrada al usuario
    jugador_movimiento = input(
        "\nIngresa el nombre del jugador para realizar un movimiento "
        "(Introduce 'Salir' para terminar): ")

    # Validar el input
    if jugador_movimiento not in ["Carlsen", "Hikaru", "Salir"]:
        print("\nNombre de jugador no válido. Inténtalo de nuevo.")
        continue

    # Verificar si el juego ha terminado
    if tiempo_carlsen <= 0 or tiempo_nakamura <= 0 or jugador_movimiento == "Salir":
        print("\n¡Partida terminada!")
        if tiempo_carlsen <= 0 and tiempo_nakamura <= 0:
            print("Empate.")
        elif tiempo_carlsen <= 0:
            print("¡Hikaru Nakamura ha ganado!")
        else:
            print("¡Magnus Carlsen ha ganado!")
        break

    # Actualizar el tiempo de acuerdo con el jugador que realizó el movimiento
    if turno_actual == "Carlsen":
        tiempo_carlsen -= tiempo_movimiento
    else:
        tiempo_nakamura -= tiempo_movimiento

    # Cambiar el turno al otro jugador
    turno_actual = "Hikaru" if turno_actual == "Carlsen" else "Carlsen"

    # Cambiar el tiempo de movimiento si uno de los jugadores alcanza 1 minuto
    if tiempo_carlsen <= 60 or tiempo_nakamura <= 60:
        tiempo_movimiento = 5

    # Pausa para simular el tiempo entre movimientos
    time.sleep(0.5)
