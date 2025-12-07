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

    #TEMP STUFF BECAUSE OLIVER WAS BORED
    #Placeholder because the empty white window scares me
    #background = tk.PhotoImage(file="../images/placeholder_background.png")

    backCanvas = tk.Canvas(gameWindow, width=800, height=600)
    backCanvas.pack(fill="both", expand=True)
    #backCanvas.create_image(0, 0, image=background, anchor="nw")

    def open_safari():
        safari.run_safari(player_data)


    open_safari()

    #def run_minigame():
    #    minigame.start_minigame()
    #savesButton = tk.Button(gameWindow, text="Test", font="Helvetica 21", command=run_minigame)
    #savesButton.place(x=165, y=515, anchor="center", height=40)
    #Make a test button that triggers the minigame thing
    #TEMP STUFF BECAUSE OLIVER WAS BORED



    # getting the current player data
    #playerData = file_IO.fetch_json("../player_data/playerData.json")[player_name]



    '''
    currentLevel = player_data["level"]
    currentCandies = player_data["candies"]
    print(currentLevel)
    print(currentCandies)

    print("Test to see if this loops over and over")
    '''

    #safari_button = tk.Button(gameWindow, text = "Safari", command = open_safari)
    #safari_button.pack()


    gameWindow.mainloop()

if __name__ == "__main__":
    pass
    #run_game("Logan") #This wont work because the argument needs a dict