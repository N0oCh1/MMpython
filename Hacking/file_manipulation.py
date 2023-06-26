import os
import sqlite3
import re
import glob
from shutil import copyfile

file_name = "#############.txt"


def create_file(desktop, history_file, steam_game):
    profile_visited = []
    with open(desktop+file_name, 'w', encoding="utf-8") as messange:
            for item in history_file:
                result = re.findall("https://www.youtube.com/@([a-zA-Z0-9]+)$",item[2])
                if result: 
                    profile_visited.append(result[0])
            messange.write("visitaste los canales :\n{}\nAdemas veo que has jugado ultimamente:\n{}".format("\n".join(profile_visited), 
                                                                                                            "\n".join(steam_game)))
    return print("the file as created")


def game_steam(steam_path):
    game = []
    game_path = glob.glob(steam_path)
    game_path.sort(key=os.path.getmtime, reverse=True)
    for a in game_path:
        game.append(a.split("\\")[-1])
    return game


def get_history(history_pacht):
    try:
        con = sqlite3.connect(history_pacht)
        connection = con.cursor()
        connection.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time ASC ")
        urls = connection.fetchall()
        con.close()
        return urls
    except sqlite3.OperationalError:
        return print("I can't connect")
    

def main():
    user_name = "C:\\Users\\"+os.getlogin()
    desktop = user_name + "\\Desktop\\"
    history_pacht = user_name + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    temp_history = history_pacht + "temp"
    copyfile(history_pacht, temp_history)
    # if you steamLibrary is diferent put on in
    steam_path = "D:\SteamLibrary\steamapps\common\*"
    chrome_history = get_history(temp_history)
    list_game_steam = game_steam(steam_path)
    print(chrome_history)
    create_file(desktop, chrome_history, list_game_steam)


if __name__ == "__main__":
    main()

