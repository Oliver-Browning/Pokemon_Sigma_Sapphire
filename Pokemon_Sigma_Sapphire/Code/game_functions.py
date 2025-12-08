import random

player_data_file = "../player_data/playerData.json"

def award_candy(current_player_data):
    """
    Generates a weighted random integer
    either 3, 5, or 10 and returns it. 
    """
    candy_amounts = [3, 5, 10]
    rand_int = random.randint(0,2)

    candy_awarded = (random.choices(candy_amounts, weights=(50, 40, 10)))[0]
    current_player_data["candies"] += candy_awarded


    return candy_awarded
    


#print(award_candy())

#import safari      #Delete this
import file_IO
import main_menu
#                            73,Geodude,100,200
def catch_pokemon(current_player_data, csvString):
    l = csvString.split(',')

    #current_player_data = #file_IO.fetch_json("../player_data/playerData.json")[main_menu.run_menu()]
              #pokedex index, Pokemon name, combat power, level
    pokemon = [l[0],l[1],random.randint( int(l[2]),int(l[3])), 1]
    current_player_data["pokemon"] += [pokemon]

    print("Inside of game_functions. Current player data: ", current_player_data)
    return pokemon, current_player_data

                #ONLY GIVEN POKEMON NAME           
def level_pokemon(pokemon_name, player_data):
    candies_available = player_data["candies"]

    #parse through data and pull out the current level
    #We will need to add pokemon level into their tracked attributes
    candies_needed = 0  #Define so we can change it in the if elif else


    selected_pokemon_data = player_data["pokemon"]
    where_is_my_pokemon = 0

    for index, value in enumerate(selected_pokemon_data):
        if pokemon_name in value:
            where_is_my_pokemon = index
    
    current_level = selected_pokemon_data["pokemon"][where_is_my_pokemon][3]

    #Determine how many candies are needed to feed the pokemon
    level_up = False

    #If level is less than 30, only 1 candy is needed to level up
    if current_level <= 30:
        candies_needed = 1
        if candies_available >= candies_needed:
            level_up = True
            candies_available -= 1

    #If level is more than 30, only 1 candy is needed to level up
    elif (current_level > 30) and (current_level <= 40):
        candies_needed = 2
        if candies_available >= candies_needed:
            level_up = True
            candies_available -= 2

    if level_up == True:
        current_level += 1
    
    #Put the new values back in
    #Write to ram
    player_data["candies"] = candies_available
    player_data["pokemon"][where_is_my_pokemon][3] = current_level

    all_player_data = file_IO.fetch_json(player_data_file)  #Convert json to dict

    #Write to disk
    save_player_data(player_data, all_player_data)


    #Then update the element in selected pokemon data that contains the level
    #With the new or same level


def save_player_data(current_player_data, all_player_data, candy_awarded = 0):

    print(f"Inside of save_player_data() BEFORE MAKING CANDY CHANGES. The current player data is: {current_player_data}")

    #Updating candies logic
    previous_candy_count = current_player_data["candies"]
    current_player_candies_updated = previous_candy_count + candy_awarded
    current_player_data["candies"] = current_player_candies_updated
    print(f"Inside of save_player_data() AFTER MAKING CANDY CHANGES. The current player data is: {current_player_data}")

    current_player_name = current_player_data["name"]

    print(f"Inside of save_player_data(). The current all_player_data is: {all_player_data}")
    all_player_data[current_player_name] = current_player_data


    file_IO.push_json(player_data_file, all_player_data, "w")




