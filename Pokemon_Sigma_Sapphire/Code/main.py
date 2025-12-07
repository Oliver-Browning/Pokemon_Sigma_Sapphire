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




player_data_file = "../player_data/playerData.json"

def main():

    all_player_data = file_IO.fetch_json(player_data_file)
    current_player_name = main_menu.run_menu()

    #print("All player data: ", all_player_data)

    if current_player_name == False:
        quit()
    elif current_player_name in all_player_data:
        current_player_data = all_player_data[current_player_name]
    else:
        print("main_menu.run_menu() has returned something invalid")
    

    print("Current player data: ", current_player_data)

    





if __name__ == "__main__":
    main()