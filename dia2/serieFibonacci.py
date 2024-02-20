#Generador de la serie de Fibonacci
#Autor: Augusto Daniel Martinez Gonzalez

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b

def main():
    n = int(input("Introduce el numero de elementos de la serie de Fibonacci: "))
    fibonacci(n)

if __name__ == "__main__":
    main()
    

