hacer = input("que deseas hacer, convertir\n introduce (CF) Celsius a Farenheit o (FC) Farenheit a Celsius\n(USE) para convertir de dolar a  euros\n")

match hacer:
    case "CF":
        ValorC = float(input("Celsius a Farenheit\n :"))
        print("su convercion de Celsius a Farenheit es: {}".format((ValorC *9/5)+32))

    case "FC":
        ValorF = float(input("Farenheit a Celsius\n :"))
        print("su convercde Farenheit a Celsius es: {}".format((ValorF-32)*5/9))
    
    case "USE":
        dolar = float(input("Dolar a Euro\n :"))
        print("su convercion de Dolar a Euro es: {}".format(dolar*0.93))
        
    case _: 
        print("introduzca la clave correctamente")