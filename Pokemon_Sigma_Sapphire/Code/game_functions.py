# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Logan Stephens
# Shreyaan Nath
# Oliver Browning
# Noam Amihai
# Section: 209
# Assignment: Team LAB 13: Part 1
# Date: 8 December 2025

import random

player_data_file = "../player_data/playerData.json"

def award_candy(current_player_data):
    """
    Takes in current_player_data (dict) as an argument and returns 
    the number of candies (int) awarded. Awards the player a random 
    amount of candy based on weighted probabilities. This function 
    selects a random candy value from 3, 5, 10, using a weighted 
    distribution of 50, 40 or 10 percent respectively. The selected 
    amount of candies is then added directly to the player's candies field.
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
    """
    Takes in current_player_data (dict) and csvString (str) and 
    returns a tuple of newly created pokemon (list) and the 
    updated current_player_data object (dict). Generates a new 
    Pokemon from a CSV string and adds it to the player's party.
    This function randomly selects a combat power with the 
    given range and assigns the Pokemon by default to level 1. 
    It then appends it to the current_player_data[“pokemon”]
    """
    l = csvString.split(',')

    #current_player_data = #file_IO.fetch_json("../player_data/playerData.json")[main_menu.run_menu()]
              #pokedex index, Pokemon name, combat power, level
    pokemon = [l[0],l[1],random.randint( int(l[2]),int(l[3])), 1]
    current_player_data["pokemon"] += [pokemon]

    print("Inside of game_functions. Current player data: ", current_player_data)
    return pokemon, current_player_data

                #ONLY GIVEN POKEMON NAME           
def level_pokemon(pokemon_name, player_data):
    """
    Takes in the pokemon_name (str) and player_data (dict). Doesn't return anything.
    Levels up the pokemon using the player's available candies.
    This function searches the player's Pokemon list for the 
    Pokemon whose pokemon_name matches any element within a pokemon entry. 
    The leveling rules are: Levels 1-30: cost is 1 candy, Levels 31-40 cost is 2 candies.
    If the player has sufficient candies, the Pokemon's level is increased by 1, 
    candies are deducted and the modified player data is saved to disk. 
    This function updates both RAM and the persistent JSON file.
    """
    candies_available = player_data["candies"]

    #parse through data and pull out the current level
    #We will need to add pokemon level into their tracked attributes
    candies_needed = 0  #Define so we can change it in the if elif else


    selected_pokemon_data = player_data["pokemon"]
    where_is_my_pokemon = 0

    for index, value in enumerate(selected_pokemon_data):
        if pokemon_name in value:
            where_is_my_pokemon = index
    
    #current_level = selected_pokemon_data["pokemon"][where_is_my_pokemon][3]
    current_level = player_data["pokemon"][where_is_my_pokemon][3]

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
    """
    Takes in current_player_data (dict), all_player_data (dict), 
    and the candy_awarded (int) and returns nothing
    Saves updated player data to the playerData.json file.
    This function optionally adds candy (candy_awarded) to the 
    player's existing candy total, updating the master player 
    dictionary and writes the modified data to the disk.
    """
    #all_player_data = all_player_data[:]

    print(f"Inside of save_player_data() BEFORE MAKING CANDY CHANGES. The current player data is: {current_player_data}")

    #Updating candies logic
    previous_candy_count = current_player_data["candies"]
    current_player_candies_updated = previous_candy_count + candy_awarded
    current_player_data["candies"] = current_player_candies_updated
    print(f"Inside of save_player_data() AFTER MAKING CANDY CHANGES. The current player data is: {current_player_data}")

    current_player_name = current_player_data["name"]

    
    all_player_data[current_player_name] = current_player_data
    print(f"Inside of save_player_data(). The current all_player_data is: {all_player_data}")

    file_IO.push_json(player_data_file, all_player_data, "w")




def active_pokemon(pokemon_name, player_data):
    """
    Takes in the pokemon_name (str) and pokemon_data (dict) and returns nothing
    Sets one of the player's Pokemon to be the active/selected pokemon
    This function locates the Pokemon whose entry contains 
    pokemon_name and assigns it to the active pokemon 
    field within player_data and writes the updated data back to disk.

    """
    print(f"Inside active_pokemon() in game_functions. pokemon_name: {pokemon_name}")
    print(f"Inside active_pokemon() in game_functions BEFORE CODE. player_data: {player_data}")

    selected_pokemon_data = player_data["pokemon"]
    where_is_my_pokemon = 0

    for index, value in enumerate(selected_pokemon_data):
        if pokemon_name in value:
            where_is_my_pokemon = index


    active_pokemon = player_data["pokemon"][where_is_my_pokemon] #Finds the pokemon matching the name and sets it to be active
    player_data["active pokemon"] = active_pokemon  #Assign the attribute active pokemon to the active pokemon
    


    all_player_data = file_IO.fetch_json(player_data_file)

    print(f"Inside active_pokemon() in game_functions AFTER CODE. player_data: {player_data}")

    save_player_data(player_data, all_player_data)

    print(f"Inside active_pokemon() in game_functions. active_pokemon: {active_pokemon}")

    
