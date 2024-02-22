def calcularINSS(salario):
    return salario * 0.07

def calcularSalario(salario):
    return salario - calcularINSS(salario)

def main():
    salario = float(input("Salario del empleado: "))
    print("Salario bruto: ", salario)
    print("INSS: ", calcularINSS(salario))
    print("El salario neto: ", calcularSalario(salario))

if __name__ == "__main__":
    main()
