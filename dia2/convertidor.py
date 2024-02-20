#convertidor de unidades de medida de almacenamiento
# Autor: Augusto Daniel Martinez Gonzalez

def convertir(opcion, cantidad):
    if opcion == 1:
        print("La cantidad de", cantidad, "kilobytes es igual a", cantidad*1024, "bytes")
    elif opcion == 2:
        print("La cantidad de", cantidad, "megabytes es igual a", cantidad*1024, "kilobytes")
    elif opcion == 3:
        print("La cantidad de", cantidad, "gigabytes es igual a", cantidad*1024, "megabytes")
    elif opcion == 4:
        print("La cantidad de", cantidad, "terabytes es igual a", cantidad*1024, "gigabytes")
    elif opcion == 5:
        print("La cantidad de", cantidad, "bytes es igual a", cantidad/1024, "kilobytes")
    elif opcion == 6:
        print("La cantidad de", cantidad, "kilobytes es igual a", cantidad/1024, "megabytes")
    elif opcion == 7:
        print("La cantidad de", cantidad, "megabytes es igual a", cantidad/1024, "gigabytes")
    elif opcion == 8:
        print("La cantidad de", cantidad, "gigabytes es igual a", cantidad/1024, "terabytes")
    else:
        print("Opcion invalida")

def menuConvertidor():
    print("Convertidor de unidades de medida de almacenamiento")
    print("*"*30)
    print("1. Convertir de kilobytes a bytes")
    print("2. Convertir de megabytes a kilobytes")
    print("3. Convertir de gigabytes a megabytes")
    print("4. Convertir de terabytes a gigabytes")
    print("5. Convertir de bytes a kilobytes")
    print("6. Convertir de kilobytes a megabytes")
    print("7. Convertir de megabytes a gigabytes")
    print("8. Convertir de gigabytes a terabytes")
    print("9. Salir")
    print("*"*30)
    opcion = int(input("Elija una opcion: "))
    return opcion

def main():
    while True:
        opcion = menuConvertidor()
        if opcion == 9:
            break
        else:
            cantidad = float(input("Introduce la cantidad: "))
            convertir(opcion, cantidad)
            print("*"*30)
            
if __name__ == "__main__":
    main()



