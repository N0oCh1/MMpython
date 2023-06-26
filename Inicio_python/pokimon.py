import random 
import os
CHARICHAR_MAX = 100
charizar = CHARICHAR_MAX
BULBASUR_MAX = 100
bulbasur = BULBASUR_MAX
Barra_HP = 20

while charizar > 0 and bulbasur > 0:
    bulbasur_atack = random.randint(1,3)

    Barra_charizar = int(charizar * Barra_HP / CHARICHAR_MAX)
    Barra_bulbasur = int(bulbasur * Barra_HP / BULBASUR_MAX)
    print ("Charizar [{}{}]  {}/{}".format( "#" * Barra_charizar, "-" * (Barra_HP - Barra_charizar), charizar , CHARICHAR_MAX))
    print ("BUlbasur [{}{}]  {}/{}".format( "#" * Barra_bulbasur, "-" * (Barra_HP - Barra_bulbasur), bulbasur , BULBASUR_MAX))
    
    print ("\nBulbasur ataca")
    #bulbasur ataca primero 
    match bulbasur_atack:
        case 1:
            #semilla 
            print("Bulbasur utiliza semilla")
            charizar -= 10
        case 2: 
            #placaje
            print("Bulbasur utiliza Placaje")
            charizar -= 15
        case 3:
            #luz solar
            print("Bulbasur utiliza Luz Solar")
            charizar -= 30
    Barra_charizar = int(charizar * Barra_HP / CHARICHAR_MAX)
    Barra_bulbasur = int(bulbasur * Barra_HP / BULBASUR_MAX)
    print ("Charizar [{}{}]  {}/{}".format( "#" * Barra_charizar, "-" * (Barra_HP - Barra_charizar), charizar , CHARICHAR_MAX))
    print ("BUlbasur [{}{}]  {}/{}".format( "#" * Barra_bulbasur, "-" * (Barra_HP - Barra_bulbasur), bulbasur , BULBASUR_MAX))
    input("enter para continuar ......\n")

    os.system("cls")

    Barra_charizar = int(charizar * Barra_HP / CHARICHAR_MAX)
    Barra_bulbasur = int(bulbasur * Barra_HP / BULBASUR_MAX)
    print ("Charizar [{}{}]  {}/{}".format( "#" * Barra_charizar, "-" * (Barra_HP - Barra_charizar), charizar , CHARICHAR_MAX))
    print ("BUlbasur [{}{}]  {}/{}".format( "#" * Barra_bulbasur, "-" * (Barra_HP - Barra_bulbasur), bulbasur , BULBASUR_MAX))
    print("""
        Tu turno de atacar

        1. Romperocas
        2. placaje
        3. Lanza llama
        4. Morrdizco

    """)

    charizar_atack = int(input(":  "))
    #charizar ataca
    match charizar_atack:
        case 1:
            #romperocas
            print("Charizar utiliza Romperocas")
            bulbasur -= 5
        case 2:
            #Placaje
            print("Charizar utiliza placaje")
            bulbasur -= 15
        case 3:
            #lanza llama
            print("Charizar utiliza lanza llama")
            bulbasur -= 50
        case 4:
            #morrdizco
            print("Charizar utiliza morrdizco")
            bulbasur -= 20
    os.system("cls")
    
Barra_charizar = int(charizar * Barra_HP / CHARICHAR_MAX)
Barra_bulbasur = int(bulbasur * Barra_HP / BULBASUR_MAX)
print ("Charizar [{}{}]  {}/{}".format( "#" * Barra_charizar, "-" * (Barra_HP - Barra_charizar), charizar , CHARICHAR_MAX))
print ("BUlbasur [{}{}]  {}/{}".format( "#" * Barra_bulbasur, "-" * (Barra_HP - Barra_bulbasur), bulbasur , BULBASUR_MAX))
if bulbasur >0:
    print("Bulbasur gana")
if charizar >0:
    print("charizar gana")
