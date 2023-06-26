import os
import random
import readchar



player_y = 1
player_x = 0
endls = 0
player_position = [5,5]
end_game = False
MAP_OBJECT = 4
#Pokemon player
PIKACHU_HP = 200
player_hp = PIKACHU_HP
#Pokemon enemig
ZUBAT_HP = 100
CATEPIE_HP = 100
RATTATA_HP = 100
PARAS_HP = 100
combat = False
enemig_hp = 100
enemig_pokemon = None
HP_VAR = 10
# map obstacle render
render_map = """\
#####               
#####               
#####        #######
#####        #######
             #######
             #######
                    
                    
##############      
##############      
##############      
##############      
##############      
                    
                    
               #####
               #####\
"""
score = 0
game_object=[]
render_map_obstacle = [list(mash) for mash in render_map.split("\n")]
Map_Width = len(render_map_obstacle[0])
Map_Height = len(render_map_obstacle)
# debug play space
print(Map_Width, Map_Height)

# put randomly game object
while len(game_object) < MAP_OBJECT:
    coordinate = [random.randint(1, Map_Width-1), random.randint(1, Map_Height-1)]
    if coordinate != player_position and coordinate not in game_object and render_map_obstacle[coordinate[1]][coordinate[0]] != "#":
        game_object.append(coordinate)
        endls += 1
    
# Render Map Game 
print (game_object)
while end_game != True:
    # drawing all objects
    print("\n")
    print ("+","-" * (Map_Width+38),"+")
    for y in range (Map_Height):
        print("|",end='')
        for x in range (Map_Width):
            char_to_draw = " "
            # draw Game_object
            for point in game_object:
                if point[0] == x and point[1] == y:
                    char_to_draw = "×"
            # player obtain point
                if point[0] == player_position[0] and point[1] == player_position[1]:
                    # Pokemons combat
                    pokemon = 0
                    os.system("cls")
                    print("######## Entraste en un combate ########")
                    # enemig pokemon choice randomly
                    pokemon = random.randint(1, 4)
                    match pokemon:
                        case 1:
                            enemig_pokemon = "Zubat"
                            enemig_hp = 100
                        case 2: 
                            enemig_pokemon = "Caterpie"
                            enemig_hp = 100
                        case 3: 
                            enemig_pokemon = "Rattata"
                            enemig_hp = 100
                        case 4:
                            enemig_pokemon = "Paras"
                            enemig_hp = 100
                    # pokemon battle start
                    print("El entrenador enemigo invoca a {}".format(enemig_pokemon))
                    print("Invocas a picachu")
                    while player_hp > 0 and enemig_hp > 0 :
                        # show HP bar
                        player_bar = int(player_hp * HP_VAR / PIKACHU_HP)
                        enemig_bar = int(enemig_hp * HP_VAR / 100)
                        print("{}  [{}{}]{}/{}".format(enemig_pokemon, "#" * enemig_bar, "-" * (HP_VAR - enemig_bar), enemig_hp, 100))
                        print("\n\nPikachu  [{}{}]{}/{}".format("#" * player_bar, "-" * (HP_VAR - player_bar), player_hp, PIKACHU_HP))
                        # player choice attack
                        print("""\n\
                        elige tu ataque:
                        1. impactrueno
                        2. placaje
                        3. bolatrueno\
                        """)
                        player_action = int(input("elige ataque: "))
                        os.system("cls")
                        match player_action:
                            case 1: 
                                print("### Pikachu utiliza impactrueno ### ")
                                enemig_hp -= (25 * random.randint(1, 2))
                            case 2:
                                print("### Pikachu utiliza Placaje ### ")
                                enemig_hp -= 10
                            case 3: 
                                print("### Pikachu utiliza Bolatrueno ### ")
                                enemig_hp -= 15
                               
                        player_bar = int(player_hp * HP_VAR / PIKACHU_HP)
                        enemig_bar = int(enemig_hp * HP_VAR / 100)
                        if player_hp < 0: 
                            player_hp = 0
                        elif enemig_hp < 0: 
                            enemig_hp = 0
                        # show HP bar
                        print("{}  [{}{}]{}/{}".format(enemig_pokemon, "#" * enemig_bar, "-" * (HP_VAR - enemig_bar), enemig_hp, 100))
                        print("\n\nPikachu  [{}{}]{}/{}".format("#" * player_bar, "-" * (HP_VAR - player_bar), player_hp, PIKACHU_HP))
                        if enemig_hp <=0: 
                            print("ganaste el combate........")
                            input("continuar.......\n")
                            break
                        else:
                            print("es turno del enemigo")
                        input("Continuar......")
                        os.system("cls")
                        # enemig randomly choice attack
                        enemig_action = random.randint(1, 3)
                        match enemig_action: 
                            case 1:
                                print("### {} utiliza Placaje ###".format(enemig_pokemon))
                                player_hp -= 10
                            case 2: 
                                print("### {} utiliza Mordizco ###".format(enemig_pokemon))
                                player_hp -= 15
                            case 3: 
                                print("### {} utiliza Ataque Especial ###".format(enemig_pokemon))
                                player_hp -= (10 + (10 * (random.randint(1, 10) / 10)))
                        if player_hp < 0: 
                            player_hp = 0
                        elif enemig_hp < 0: 
                            enemig_hp = 0
                        # show HP bar
                        player_bar = int(player_hp * HP_VAR / PIKACHU_HP)
                        enemig_bar = int(enemig_hp * HP_VAR / 100)
                        print("{}  [{}{}]{}/{}".format(enemig_pokemon, "#" * enemig_bar, "-" * (HP_VAR - enemig_bar), enemig_hp, 100))
                        print("\n\nPikachu  [{}{}]{}/{}".format("#" * player_bar, "-" * (HP_VAR - player_bar), player_hp, PIKACHU_HP))
                        input("Continuar......")
                        if player_hp < 0 :
                            break
                        os.system("cls")
                    if enemig_hp <= 0: 
                        game_object.remove(player_position)
                        score +=1
                    elif player_hp <= 0: 
                        game_object.remove(player_position)
                        print("####### Game Over #######")
                        end_game = True
            # draw player in position
            if player_position[player_x] == x and player_position[player_y] == y:
                char_to_draw = "☺"
            # draw wall game
            if render_map_obstacle[y][x] == '#':
                char_to_draw = "■"

            print(" {} ".format(char_to_draw), end="")
        print("|")
    print ("+","-" * (Map_Width+38),"+")


#get a point/ Debug Log
    print (score)
    print("debug Log:")
    print ("player position = {}".format(player_position))
    print ("object coordinate = {}".format(game_object))

# Player movement
    player_movement = readchar.readchar()
    print (player_movement)
    new_position = None
    match player_movement:
        case "w": 
            new_position = [player_position[player_x], (player_position[player_y]-1)%Map_Height]
        case "s":
            new_position = [player_position[player_x], (player_position[player_y]+1)%Map_Height]
        case "a":
            new_position = [(player_position[player_x]-1) % Map_Width, player_position[player_y]]
        case "d":
            new_position = [(player_position[player_x]+1) % Map_Width, player_position[player_y]]
        case "q":
            end_game = True
    if new_position:
        if render_map_obstacle[new_position [1]][new_position[0]] != "#":
            player_position = new_position
    
    #end game when get all point
    if score == MAP_OBJECT: 
        print("##### You Win #####")
        end_game = True
        input()
    os.system("cls")

    

