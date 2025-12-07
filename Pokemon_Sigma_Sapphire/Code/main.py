'''
import keyboard
import os
import time
import msvcrt
'''
import game
import main_menu
import file_IO


#Change read file path as needed for your file system
#global read_path
read_path = "Pokemon_Sigma_Sapphire\\PokeList_v3.csv"

'''
game board:
1====================================================================================================         100 ='s
2  Player_name                                  stuff                                     p - pause 
3====================================================================================================
4                                                                                                    
5                                                                                                   
6                                                                                                   
7                                                                                                   
8                                                                                                   
9                                                                                                   
0                                                                                                   
1                                                                                                   
2                                                                                                   
3                                                                                                   
4                                                                                                   
5                                                                                                                                          Actual game stuff
6                                                                                                   
7                                                                                                   
8                                                                                                   
9                                                                                                   
0                                                                                                   
1                                                                                                   
2                                                                                                   
3                                                                                                   
4                                                                                                   
5                                                                                                   
6                                                                                                   
7                                                                                                   
8                                                                                                   
9                                                                                                   
0====================================================================================================
1                                            Example
2   
3
4   Option 1.                    Option 5.        
5   Option 2.                    Option 6.
6   Option 3.                    Option 7.
7   Option 4.                    Option 8.
8 
9
0====================================================================================================
'''



#player_file_locations = ["../player_data/noam.json", "../player_data/oliver.json", "../player_data/logan.json", "../player_data/shreyaan.json"]
player_file_location_dict = {"noam": "../player_data/noam.json", 
                             "oliver": "../player_data/oliver.json",
                             "logan": "../player_data/logan.json",
                             "shreyaan": "../player_data/shreyaan.json"
                             }


def main():

    current_player_name = main_menu.run_menu()
    print("Before if statements", current_player_name)
    if current_player_name == False:
        quit()
    elif current_player_name in player_file_location_dict.keys():
        current_player_name = current_player_name.lower()
        current_player_file = player_file_location_dict[current_player_name]
    else:
        print("main_menu.run_menu() has returned something invalid")
    print("After if statements", current_player_name)
    print("Current player file", current_player_file)
    current_player_data = file_IO.fetch_json(current_player_file)

    print("DATA after file statements", current_player_data)

    
    #Load player json
    





    




if __name__ == "__main__":
    main()