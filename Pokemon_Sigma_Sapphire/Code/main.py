import game_window
import main_menu
import file_IO
import random
import game_functions

#The different file paths for the json and csv files
poke_list_path = "../PokeList_v3.csv"
player_data_file = "../player_data/playerData.json"

def main():
    """
    This function takes in no arguments. It calls all of the
    other functions to make the program work as well as assign
    some of the necessary primary variables like player data
    and the pokemon csv.
    """



    poke_list = file_IO.fetch_list(poke_list_path, False)   #Get list of pokemon
    all_player_data = file_IO.fetch_json(player_data_file)  #Convert json to dict

    # the whole thing is put into a while true, that way it keeps returning to the main menu until quit is pressed!
    while True:
        current_player_name = main_menu.run_menu()  #Get current player from UI



        #Check if main_menu.run_menu() returns false since that indicates quit game was selected
        if current_player_name == False:
            quit()
        #Check to see if the name returned actually exists just in case an error occurs between the UI and this file
        elif current_player_name in all_player_data:
            current_player_data = all_player_data[current_player_name]

            #Check if the player has any pokemon, and if not, they are assigned a random pokemon
            if len(current_player_data["pokemon"]) == 0:
                #poke_list_1 = file_IO.fetch_list("../PokeList_v3.csv", False)
                game_functions.catch_pokemon(current_player_data, poke_list[random.randint(1,150)])

        else:   #For debugging
            print("main_menu.run_menu() has returned something invalid")

        #player_data_file = "../player_data/playerData.json"
        #all_player_data = file_IO.fetch_json(player_data_file)
        #print(f"ALL PLAYER DATA: {all_player_data}")
        game_functions.save_player_data(current_player_data, all_player_data)


        #Debug print statements
        print("Current player data: ", current_player_data)
        print("Current player data type: ", type(current_player_data))



        #Run the game display function
        game_window.run_game(current_player_data, all_player_data)
    


if __name__ == "__main__":
    main()