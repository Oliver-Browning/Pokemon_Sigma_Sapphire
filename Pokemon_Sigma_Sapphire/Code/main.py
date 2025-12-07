'''
import keyboard
import os
import time
import msvcrt
'''
import game_window
import main_menu
import file_IO

read_path = "../PokeList_v3.csv"
player_data_file = "../player_data/playerData.json"

def main():
    """
    This function takes in no arguments. It calls all of the
    other functions to make the program work as well as assign
    some of the necessary primary variables like player data
    and the pokemon csv.
    """


    all_player_data = file_IO.fetch_json(player_data_file)
    current_player_name = main_menu.run_menu()


    #Check if main_menu.run_menu() returns false since that indicates quit game was selected
    if current_player_name == False:
        quit()
    #Check to see if the name returned actually exists just in case an error occurs between the UI and this file
    elif current_player_name in all_player_data:
        current_player_data = all_player_data[current_player_name]
    else:   #For debugging
        print("main_menu.run_menu() has returned something invalid") 
    #print("Current player data: ", current_player_data) #For debugging

    #Do other stuff before starting game
    #game()


if __name__ == "__main__":
    main()