import tkinter as tk
import skyblockPuzzle
import file_IO
import random
import game_functions


def run_safari(player_data):




    safari_window = tk.Tk()

    safari_window.geometry("800x600")
    safari_window.resizable(False, False)
    safari_window.title("Safari")


    poke_list_1 = file_IO.fetch_list("../PokeList_v3.csv", False)

    #selected_pokemon = poke_list_1[random.randint(1,150)]
    


    weirdo_tuple = skyblockPuzzle.three_weirdos()


    weirdo_1_name = weirdo_tuple[0][0]       
    weirdo_1_dialogue = weirdo_tuple[0][1]      #Write this to tkinter, Noam

    weirdo_2_name = weirdo_tuple[1][0]  
    weirdo_2_dialogue = weirdo_tuple[1][1]      #Write this to tkinter, Noam

    weirdo_3_name = weirdo_tuple[2][0]
    weirdo_3_dialogue = weirdo_tuple[2][1]      #Write this to tkinter, Noam

    game_won = False




    def option_selected(num):
        """
        Words
        """
        if num == 1:
            game_won = weirdo_tuple[0][2]   #Extract boolean from index of tuple
            print(game_won)     #For debugging
        elif num == 2:
            game_won = weirdo_tuple[1][2]   #Extract boolean from index of tuple
            print(game_won)     #For debugging
        elif num == 3:
            game_won = weirdo_tuple[2][2]
            print(game_won)
        else:
            print("Something has gone very wrong with option_selected()")

        #Check if game has been won, if so, pick a random pokemon and add it to the player's pokedex
        if game_won == True:
            newly_caught_pokemon = game_functions.catch_pokemon(player_data, poke_list_1[random.randint(1,150)])

            #Assign the different pieces of info about the newly caught pokemon to their respective variables
            pokedex_number = int(newly_caught_pokemon[0])
            pokemon_name = newly_caught_pokemon[1]
            combat_power = newly_caught_pokemon[2]

            #Display some information about the newly caught pokemon
            print(f"You caught pokemon #{pokedex_number}!!!")                   #Write this to tkinter, Noam
            print(f"The name of the pokemon you caught is: {pokemon_name}!!!")  #Write this to tkinter, Noam
            print(f"The combat power of {pokemon_name} is: {combat_power}!!!")  #Write this to tkinter, Noam
        



    option_1 = tk.Button(safari_window, text = weirdo_1_name, command = lambda: option_selected(1))
    option_2 = tk.Button(safari_window, text = weirdo_2_name, command = lambda: option_selected(2))
    option_3 = tk.Button(safari_window, text = weirdo_3_name, command = lambda: option_selected(3))
    #option_4 = tk.Button(safari_window, text = game_won)

    #T = tk.Text(safari_window, height = "5", width = "10")
    lab = tk.Label(safari_window, text=game_won)

    option_1.pack()
    option_2.pack()
    option_3.pack()
    lab.pack()

    #   139,Kabuto,170,270

    safari_window.mainloop()

if __name__ == "__main__":
    run_safari()

    #print(help(tk.Button()))