#Calcular la velocidad de un objeto
# v = d/t
# d = v*t
# t = d/v
import os
os.system('clear||cls')
print("Calcular la velocidad, distancia y tiempo de un objeto")
print("*"*30)
print("1. Calcular la velocidad")
print("2. Calcular la distancia")
print("3. Calcular el tiempo")
print("4. Salir")
opcion = int(input("Elija una opcion: "))
if opcion == 4:
    print("Adios")
else:
    if opcion == 1:
        distancia = float(input("Introduce la distancia recorrida: "))
        tiempo = float(input("Introduce el tiempo: "))
        print("La velocidad es: ", distancia / tiempo)
    elif opcion == 2:
        velocidad = float(input("Introduce la velocidad: "))
        tiempo = float(input("Introduce el tiempo: "))
        print("La distancia recorrida es: ", velocidad * tiempo)
    elif opcion == 3:
        distancia = float(input("Introduce la distancia recorrida: "))
        velocidad = float(input("Introduce la velocidad: "))
        print("El tiempo es: ", distancia / velocidad)
    else:
        print("Opcion invalida")

print("*"*30)
