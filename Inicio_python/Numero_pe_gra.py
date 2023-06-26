
lista = []

usuario = input("introduzca la los numeros con una coma (ejem: 1,2,3,4,5,6) : ")
lista = [int(numero) for numero in usuario.split(",")]
cantidad = len(lista)

for posicion in range(0,cantidad):
    for a in range(0,cantidad):
        if lista[posicion] < lista[a]:
            tem = lista[posicion]
            lista[posicion] = lista[a]
            lista[a] = tem
print ("El numero menor es : {}".format(lista[0]))
print ("El numero mayor es : {}".format(lista[cantidad-1]))
print (lista)