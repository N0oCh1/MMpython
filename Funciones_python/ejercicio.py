def main():
    print("""
    1. string mas largo
    2. sumando la lista
    3. par o impar
    4. preunta algo
    5. A mayus
    6. adivina el numero
    7. lista de la compra
    """)
    opcion = int(input("que ejercicio quieres ejecutar: "))
    match opcion:
        case 1: 
            string_largo("holas", "largo", "muchoMas")
        case 2: 
            sumando_lista()
        case 3: 
            Par_impar()
        case 4: 
            preguta()
        case 5: 
            mayus()
        case 6: 
            adivinar()
        case 7: 
            lista()


def string_largo(*args):
    if args:
        for a in args:


    print(args) 




if __name__ == "__main__":
    main()