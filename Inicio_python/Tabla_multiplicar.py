import math

numero = 0
respuesta = 0
print ("introduzca un numero para mostrar una tabla de multiplicar del numero:  ")
numero = int(input("Tabla de multiplicar del numero: "))
for a in range(1,11):
    respuesta = numero * a
    print (" {} x {} = {} ".format(numero, a, respuesta))