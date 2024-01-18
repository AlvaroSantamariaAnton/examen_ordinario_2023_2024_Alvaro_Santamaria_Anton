
while True:
    try:
        numero_elegido = int(input("\nIngrese un número entero mayor o igual a 1: "))

        if numero_elegido <= 0:
            print("\nPor favor, introduce un número valido.")
        else:
            print(f"\nTu pirámide tendrá {numero_elegido} alturas.")
            break
    except ValueError:
        print("\nPor favor, introduce un número valido.")

print("\n" + "*")
numero_niveles = 0
while True:
    numero_niveles += 1
    if numero_niveles == numero_elegido + 1:
        break
    else:
        print("\n" + "*" * numero_elegido)