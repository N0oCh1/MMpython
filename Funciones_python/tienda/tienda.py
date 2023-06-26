import time
href = "D:\Proyectos\Mastermind\MMpython\Funciones_python\Tienda\save.txt"
EXIT = "salida"



def main():
    shopping_list = load_list()
    user_input = None
    print("debug: {}".format(shopping_list))
    while user_input != EXIT:
        user_input = put_something()
        put_on_the_list(user_input, shopping_list)
    save_list(shopping_list)
    show_list()


def put_something():
    return input("introduce el item [{}] para salir:  ".format(EXIT)).lower()


def show_list():
    with open(href, "r") as save:
        return print("esta es tu lista:\n{}".format(save.read()))


def save_list(shopping_list):
    shopping_list.pop()
    with open(href, "w") as save:
        save.write("\n".join(shopping_list))


def load_list():
    shopping_list = []
    if input("quieres cargar lista anterior [S/N]:  ").lower() == "s":
        try:
            with open(href, "r") as save:  
                shopping_list = save.read().split("\n")
            print("lista cargada exitosamente!")
            time.sleep(1)
            show_list()
        except FileNotFoundError:
            print("no hay lista guardadas!")
    return shopping_list


def put_on_the_list(user_input, shopping_list):

        if user_input.lower() in [a.lower() for a in shopping_list] :
            print("El item ya esta en la lista!")
        else: 
            shopping_list.append(user_input)


if __name__ == "__main__":
    main()





