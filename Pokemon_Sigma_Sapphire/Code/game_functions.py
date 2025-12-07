import random

def award_candy():
    """
    Takes in no arguments. Generates a weighted random integer
    either 3, 5, or 10 and returns it. 
    """
    candy_amounts = [3, 5, 10]
    rand_int = random.randint(0,2)

    candy_awarded = (random.choices(candy_amounts, weights=(50, 40, 10)))[0]

    return candy_awarded
    


#print(award_candy())

import safari
import file_IO
import main_menu

def catch_pokemon(current_player_data, csvString):
    l = csvString.split(',')

    #current_player_data = #file_IO.fetch_json("../player_data/playerData.json")[main_menu.run_menu()]
    
    current_player_data["pokemon"] += [[l[0],l[1],random.randint( int(l[2]),int(l[3]) )]]

    print(current_player_data)
