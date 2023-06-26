import PySimpleGUI as sg


def main():
    # all parameter for Tic Tac Touch
    sg.theme('DarkAmber')
    win_state =[(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]
    game_over = False
    PLAYER_ONE = "X"
    PLAYER_TWO = "O"
    current_player = PLAYER_ONE
    button_size = (8,4)
    event = "-REPEAT-" 
    while event == "-REPEAT-":
        window = window_set_layout(tictactou(button_size))
        event = game_logic(window, PLAYER_ONE, PLAYER_TWO, win_state,current_player)
        window.close()
    window.close()

# nueva cosa

def cualquiera_cosa():
    pass


def tictactou(button_size):
    layout = [
                [sg.Text("player 1 go first", text_color = "red", size=(40,1), key = "-PLAYER-")],
                [
                sg.Button("", size=button_size, key="-1-"), 
                sg.Button("", size=button_size, key='-2-'), 
                sg.Button("", size=button_size, key='-3-')
                ],
                [
                sg.Button("", size=button_size, key='-4-'), 
                sg.Button("", size=button_size, key='-5-'), 
                sg.Button("", size=button_size, key='-6-')
                ],
                [
                sg.Button("", size=button_size, key='-7-'), 
                sg.Button("", size=button_size, key='-8-'), 
                sg.Button("", size=button_size, key='-9-')
                ],
                [sg.Text(size=(40,1), key = "-OUTPUT-")],
                [sg.Button("cancel", key='-STOP-'), sg.Button("repeat", key="-REPEAT-")]
            ]     
    return layout         
                            

def window_set_layout(layout):
    window = sg.Window("tres en raya", layout)
    return window


def game_logic(window, PLAYER_ONE, PLAYER_TWO, win_state, current_player):
    game_over = False
    while True:
        event, value = window.read()
        
        if game_over:
            if window.Element(event).ButtonText == "":
                pass
            if event == sg.WIN_CLOSED or event == "-STOP-" or event == "-REPEAT-":
                break
        if event == sg.WIN_CLOSED or event == "-STOP-" or event == "-REPEAT-":
            break
        if window.Element(event).ButtonText == "" and game_over == False:
            window["-PLAYER-"].update("player 2 go", text_color = "blue")
            window.Element(event).update(text = current_player)
            if current_player == PLAYER_ONE:
                window["-PLAYER-"].update("player 2 go", text_color = "blue")
                current_player = PLAYER_TWO
            else:
                window["-PLAYER-"].update("player 1 go", text_color = "red")
                current_player = PLAYER_ONE
            print (event, value)
            for a in win_state:
                player_one = 0
                player_two = 0
                for b in a:
                    position = str("-{}-".format(b))
                    if window.Element(position).ButtonText == PLAYER_ONE:
                        player_one += 1
                        if player_one == 3:
                            window["-OUTPUT-"].update("player 1 win", text_color = "green")
                            game_over = True
                    if window.Element(position).ButtonText == PLAYER_TWO:
                        player_two += 1
                        if player_two == 3:
                            window["-OUTPUT-"].update("player 2 win", text_color = "green")
                            game_over = True
    return event


if __name__ == "__main__":
    main()