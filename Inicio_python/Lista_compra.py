import os
lista = []
condicion = ""
print(
    """lista de compras"""

)
while condicion != ("q" or "Q") :

    condicion = input("introduce el item para la lista (Q para mostrar la lista):  ")
    if condicion in lista :
        os.system("cls")
        print("##### EL ITEM YA ESTA EN LA LISTA #####")

    else :
        os.system("cls")
        print("##### EL ITEM SE GUARDO EN LA LISTA #####")
        lista.append(condicion)
lista.pop()
print("esta es su lista\n {}".format(lista))