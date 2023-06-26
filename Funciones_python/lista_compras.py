def main():
    SALIR = "salida"
    input_usuario = None
    lista = []
    while input_usuario != SALIR:
        input_usuario = input("introduce los objetos de compra ({} para salir):  ".format(SALIR))
        lista.append(input_usuario)
        print("\n".join(lista))
    lista.pop()
    nombre = input("que nombre le pondra a la lista:  ")
    guardar(lista, nombre)


def guardar(lista, nombre):
    a = open("{}.txt".format(nombre), "w")
    a.write("\n" .join(lista))
    a.close()


if __name__ =="__main__":
    main()