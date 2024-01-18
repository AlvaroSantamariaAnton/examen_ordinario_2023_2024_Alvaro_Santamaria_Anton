# Bucle principal para asegurar la correcta entrada inicial
while True:
    try:
        numero_elegido = int(input("\nIngrese un número entero mayor o igual a 1: "))

        if numero_elegido <= 0:
            print("\nPor favor, introduce un número valido.")
        else:
            print(f"\nTu pirámide de {numero_elegido} niveles está lista.")
            break
    except ValueError:
        print("\nPor favor, introduce un número valido.")

print()

espacios = numero_elegido - 1
asteriscos = 1

# Bucle for para crear y mostrar las alturas
for i in range(numero_elegido):
     
    print(" " * espacios + "*" * asteriscos)
    espacios -= 1
    asteriscos += 2    