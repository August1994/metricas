#Calculadora sencilla
#Autor: Augusto Daniel Martinez Gonzalez

print("Calculadora sencilla -  Operaciones Matematicas")
print("*"*30)
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Salir")

opcion = int(input("Elija una opcion: "))
if opcion == 5:
    print("Adios")
else:
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    if opcion == 1:
        print("La suma es: ", num1 + num2)
    elif opcion == 2:
        print("La resta es: ", num1 - num2)
    elif opcion == 3:
        print("La multiplicacion es: ", num1 * num2)
    elif opcion == 4:
        print("La division es: ", num1 / num2)
    else:
        print("Opcion invalida")
print("*"*30)
