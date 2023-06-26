def main():
    print("###### calculadora ######")
    n1 = int(input("numero 1:  "))
    n2 = int(input("numero 2:  "))

    print("""
    + sumar 
    - restar 
    * multiplicar
    """)
    operador = input(": ")
    match operador: 
        case "+": 
            respueta = suma(n1, n2)
        case "-":
            respueta = resta(n1, n2)
        case "*":   
            respueta = multiplicar(n1, n2)
    print(" su calculo es:  {}".format(respueta))


def suma(n1, n2):
    resultado = n1 + n2
    return resultado


def resta(n1, n2):
    resultado = n1 - n2 
    return resultado


def multiplicar(n1, n2):
    resultado = n1 * n2 
    return resultado


if __name__ == "__main__": 
    main()
