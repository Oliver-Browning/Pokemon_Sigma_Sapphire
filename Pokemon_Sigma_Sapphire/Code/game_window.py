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


    # generating the main map frame
    mainMapFrame = tk.Frame(gameWindow)
    mainMapFrame.pack(fill="both", expand=True)
    mapCanvas = tk.Canvas(mainMapFrame, width=800, height=600)
    mapCanvas.pack(fill="both", expand=True)
    map = tk.PhotoImage(file="../Images/map.png")
    mapCanvas.create_image(0, 0, image=map, anchor="nw")

    # help house
    helpHouseImage = tk.PhotoImage(file="../Images/help_House.png")
    helpHouseButton = tk.Button(mainMapFrame, image=helpHouseImage, activebackground="sky blue", relief="flat")
    helpHouseButton.place(x=160, y=435, anchor="center", width=97, height=129)

    # arena
    arenaImage = tk.PhotoImage(file="../Images/Arena.png")
    arenaButton = tk.Button(mainMapFrame, image=arenaImage, activebackground="sky blue", relief="flat")
    arenaButton.place(x=640, y=430, anchor="center", width=192, height=130)


    gameWindow.mainloop()

if __name__ == "__main__":
    run_game("Noam")