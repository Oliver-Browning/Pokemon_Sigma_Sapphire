import tkinter as tk
import file_IO
import game_functions

def run_game(player):

    # the usual general setup
    gameWindow = tk.Tk()
    gameWindow.title("Pokemon Sigma Sapphire: " + player)
    gameWindow.resizable(False, False)
    gameWindow.geometry("800x600")


    # getting the current player data
    playerData = file_IO.fetch_json("../player_data/playerData.json")[player]
    currentLevel = playerData["level"]
    currentCandies = playerData["candies"]
    print(currentLevel)
    print(currentCandies)


    gameWindow.mainloop()

if __name__ == "__main__":
    run_game("Logan")