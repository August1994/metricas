#Generador de tablas de multiplicar de un numero
#Autor: Augusto Daniel Martinez Gonzalez

def tablaMultiplicar(numero):
    for i in range(1,13):
        print(f"{numero :>3} * {i :>3} = {(numero*i) :>3}")
              
def main():
    numero = int(input("Introduce el numero del cual quieres la tabla de multiplicar: "))
    tablaMultiplicar(numero)

if __name__ == "__main__":
    main()