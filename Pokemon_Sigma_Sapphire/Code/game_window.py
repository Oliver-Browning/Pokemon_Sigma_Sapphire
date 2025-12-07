import tkinter as tk
import file_IO
import game_functions

def run_game(player_data):

    player_name = player_data["name"]


    # the usual general setup
    gameWindow = tk.Tk()
    gameWindow.title("Pokemon Sigma Sapphire: " + player_name)
    gameWindow.resizable(False, False)
    gameWindow.geometry("800x600")


    # getting the current player data
    #playerData = file_IO.fetch_json("../player_data/playerData.json")[player_name]
    currentLevel = player_data["level"]
    currentCandies = player_data["candies"]
    print(currentLevel)
    print(currentCandies)


    gameWindow.mainloop()

if __name__ == "__main__":
    pass
    #run_game("Logan") #This wont work because the argument needs a dict