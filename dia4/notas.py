#Calcular la nota final de un estudiante
#Entradas: 3 notas parciales
#Salidas: nota final

def calcularNotaFinal(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def main():
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    print("Nota final: ", calcularNotaFinal(nota1, nota2, nota3))

if __name__ == "__main__":
    main()
