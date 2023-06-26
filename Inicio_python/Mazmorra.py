#zona de declaraciones
import random

bate_carton = False
pedazo_carton = False
pistola_carton = False
frase_arma = ""
azul = True
valor1 = random.randint(1,100)
valor2 = random.randint(1,100)
# panel 1
print ("""
Fuiste secuestrado por "EL" nadie sabe quien es, pero se sabe que le 
gusta hacer mazmorra de carton y fuiste elegido por "EL" para su juegos macabros.
""")
input("\n enter para continuar")
print ("""
\n\nCuando te secuestraron quedaste inconsiente, al despertar te encuentras con 
dos puerta de carton pintado. cual eliges?\n\nA. puerta de carton amarillo 
\nB. puerta de carton azul
""")
puerta = input("\ncual eliges:  ")
if puerta == ("a" or "A"):
#pane 2
    print ("""
    entraste por la puerta amarillo y te encuentras con un habitacion sin salida y 
    en el centro una mesa con tres objetos que elegiras?\n\n    
    A.  bate de cartulina
    B.  un pedazo de carton
    C.  una pistola de carton
    D.  te das la media vuelta y te vas
    """)
    opcion_arma = input("\n\ncual eliges  :")
    match opcion_arma: 
        case "A":
            bate_carton = True
            print ("\nagarras el bate de cartulina y te vas de la habitacion")
        case "a":
            bate_carton = True
            print ("\nagarras el bate de cartulina y te vas de la habitacion")
        case "B":
            pedazo_carton = True
            print ("\nagarras el pedazo de carton y te vas de la habitacion")
        case "b":
            pedazo_carton = True
            print ("\nagarras el pedazo de carton y te vas de la habitacion")
        case "C":
            pistola_carton = True
            print ("\nagarras la pistola de carton y te vas de la habitacion")
        case "c":
            pistola_carton = True
            print ("\nagarras la pistola de carton y te vas de la habitacion")
        case "D":
            print ("\nte das la media vuelta y regresa")
        case "d":
            print ("\nte das la media vuelta y regresa")
    print (
    """regresaste a la habitacion en la que quedaste inconsiente, solo te queda una puerta 
    por elegir """)
    print ("""\n
       puerta de carton amarillo #
    B. puerta de caton azul""")
    input("\nCual eliges: ")

print (
"""\nentras por la puerta azul 
te encuentras con una habitacion aparentemente vacia, tu decides mirar arriba y 
te encuentras con un techo lleno de Legos, quieres retroceder pero no puedes 
(la puerta esta trancada) y tu unica salida es una puerta con un panel de carton
que tiene escrito lo siguente 'ante la salida, resuelve este escrito o el cielo te 
caera encima'"""
    )
respuesta = int(input("\n{} + {} = ".format(valor1, valor2)))
if respuesta == (valor1 + valor2):
    print ("""Respondiste de manera correcta y la puerta se abre y pasas por ella.
    en la habitacion te encuentras con un golem de carton controlado por "EL" 
    que custodia la puerta de la salida. que haras?"""
    )
    if bate_carton == True:
        print("""
        A. Bate de cartulina
        B. no hacer nada 
        """)
        if input("\n que hacer: ") == ("a"or"A"):
            print("""
            utiliza el bate de cartulina y te conviertes en un verdadero Jedi y derrotas al 
            golem de carton incluyendo a "EL" y sales por la puerta custodiado. GANASTE.
            

            ############ Good Ending. Carton bajo el sol ############
            """)
            input("\n")
        else:
            print("""
            Tu pereza te gana y no haces nada, el golem te aplasta....


            ############ Bad Ending. La especialidad de este animal es hacer NADA ############
            """)
            input("\n")
    if pedazo_carton == True:
        print("""
        A. Pedazo de carton
        B. no hacer nada"""
        )
        if input("\n que hacer: ") == ("a"or"A"):
            print("""
            utilizas el pedazo de carton lanzandolo hacie el golem, no le haces nada... "EL" y el golem se quedan en ._. y te 
            aplasta cuestionando tu inteligencia pero no tu valor.

            
            ############ Bad Ending. no es bueno comer crayones ############
            """)
            input("\n")
        else:
            print("""
            Tu pereza te gana y no haces nada, el golem te aplasta....


            ############ Bad Ending. La especialidad de este animal es hacer NADA ############
            """)
            input("\n")

    if pistola_carton == True:
        print("""
        A. Pistola de carton
        B. no hacer nada
        """)
        if input("\n que hacer: ") == ("a"or"A"):
            print("""
            utiliza la pistola de carton y te cres John Wick derrotando al golem con tres balas y dos para "EL"... 
            pero solo fue tu imaginacion porque la pistola es de carton... "EL" y el golem cuestionan tus delirios 
            y te aplasta, hey que pistola mas guay (̿̿ ̿̿ ̿̿ ̿̿\̵͇̿̿\).


            ############ Bad Ending. Piuw Piuw Piuw Piuw Piuw ############
            """)
            input("\n")
        else:
            print("""
            Tu pereza te gana y no haces nada, el golem te aplasta....


            ############ Bad Ending. La especialidad de este animal es hacer NADA ############
            """)
            input("\n")            
    if (pistola_carton or bate_carton or pedazo_carton) != True:
        print(""" 
        \nA. ._.
        """)
        input("\n._. ")
        print("""
        al no tener nada con que pelear el golem te aplasta matandote, mientras "EL" habla 'si hubieras traido
        algo para defenderte, podrias haber hecho algo'.
        PoV Golem 
        aplastar AmaRillo JelioW 


        ############ Bad Ending. XD ############
        """)
        input("\n")     
else:
    print ("""respondiste de manera incorrecta y el cielo de Lego caen sobre ti, no mueres 
    por los legos pero, la habitacion se convierte en una mina de cubitos de lego al 
    saber que pisar los Legos es doloroso, mueres de desidratacion por no poder moverte 
    entre los Legos.
    

    ############ Bad Ending. Plastic, Plasta, Morto ############
    """
    )
    input("\n")