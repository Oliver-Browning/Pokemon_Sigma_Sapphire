import tkinter as tk
import file_IO
import game_functions
import safari
import minigame

def run_game(player_data):

    player_name = player_data["name"]


    # the usual general setup
    gameWindow = tk.Tk()
    gameWindow.title("Pokemon Sigma Sapphire: " + player_name)
    gameWindow.resizable(False, False)
    gameWindow.geometry("800x600")


    gameWindow.mainloop()

if __name__ == "__main__":
    pass
    #run_game("Logan") #This wont work because the argument needs a dict