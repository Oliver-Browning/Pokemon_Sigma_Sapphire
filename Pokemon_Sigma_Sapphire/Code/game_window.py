import tkinter as tk
import file_IO
import game_functions
import safari

def run_game(playerData):

    # the usual general setup
    gameWindow = tk.Tk()
    gameWindow.title("Pokemon Sigma Sapphire: " + playerData["name"])
    gameWindow.resizable(False, False)
    gameWindow.geometry("800x600")


    # getting the current player data
    currentLevel = playerData["level"]
    currentCandies = playerData["candies"]
    print(currentLevel)
    print(currentCandies)


    # this function handles entering the tutorial house!
    def tutorial_house_enter():
        mainMapFrame.place_forget()
        helpHouseFrame.place(x=0, y=0, relwidth=1, relheight=1)

    def tutorial_house_leave():
        helpHouseFrame.place_forget()
        mainMapFrame.place(x=0, y=0, relwidth=1, relheight=1)











    ##### generating the main map frame
    mainMapFrame = tk.Frame(gameWindow)
    mainMapFrame.place(x=0, y=0, relwidth=1, relheight=1)
    mapCanvas = tk.Canvas(mainMapFrame, width=800, height=600)
    mapCanvas.pack(fill="both", expand=True)
    map = tk.PhotoImage(file="../Images/map.png")
    mapCanvas.create_image(0, 0, image=map, anchor="nw")

    # help house
    helpHouseImage = tk.PhotoImage(file="../Images/help_House.png")
    helpHouseButton = tk.Button(mainMapFrame, image=helpHouseImage, activebackground="sky blue", relief="flat", command=tutorial_house_enter)
    helpHouseButton.place(x=160, y=435, anchor="center", width=97, height=129)

    # arena
    arenaImage = tk.PhotoImage(file="../Images/Arena.png")
    arenaButton = tk.Button(mainMapFrame, image=arenaImage, activebackground="sky blue", relief="flat")
    arenaButton.place(x=640, y=430, anchor="center", width=192, height=130)

    # safari
    safariButton = tk.Button(mainMapFrame, text="safari", activebackground="sky blue", relief="flat", command=lambda: safari.run_safari(playerData))
    safariButton.place(relx=0.2, rely=0.2, anchor="center")


    ##### generating the tutorial house frame
    helpHouseFrame = tk.Frame(gameWindow)
    # helpHouseFrame.place(x=0, y=0, relwidth=1, relheight=1)
    helpHouseCanvas = tk.Canvas(helpHouseFrame, width=800, height=600)
    helpHouseCanvas.pack(fill="both", expand=True)
    helpHouseEntryImage = tk.PhotoImage(file="../Images/mainMenu_Background.png")
    helpHouseCanvas.create_image(0, 0, image=helpHouseEntryImage, anchor="nw")
    helpHouseExitButton = tk.Button(helpHouseFrame, text="exit", command=tutorial_house_leave)
    helpHouseExitButton.place(relx=0.5, rely=0.9, anchor="center")



    gameWindow.mainloop()
