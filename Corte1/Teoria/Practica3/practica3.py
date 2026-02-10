while True:

    a = input("Por favor ingrese un valor: ")
    aInt = int(a)
    mod = aInt % 2

    if (mod == 0):
        print("a es un PAR")
    else:
        print("a es un IMPAR")

    continuar = input("¿Desea continuar? (si/no): ")

    if continuar == "no":
        print("Saliendo del programa")
        break

    