#calcular el iva de un producto

def calcular_iva(precio, iva):
    return precio * iva

def calcular_precio(precio, iva):
    return precio + calcular_iva(precio, iva)

def main():
    precio = float(input("Precio del producto: "))
    iva = 0.16
    print("El precio con iva es: ", calcular_precio(precio, iva))

if __name__ == "__main__":
    main()
    