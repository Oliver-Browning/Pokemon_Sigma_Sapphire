import tkinter as tk
import file_IO
import game_functions
import safari
import button_glow
import skyblockPuzzle
import random

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

    # this function handles entering the safari!

    def safari_enter():
        # switch frames
        mainMapFrame.place_forget()
        safariFrame.place(x=0, y=0, relwidth=1, relheight=1)

        # show the initial confrontation things!
        confrontButton.place(relx=0.5, rely=0.8, anchor="center", height=40)
        teamRocketBlocksLabel.place(relx=0.5, rely=0.1, anchor="n")

        # safari.run_safari(playerData)


    def safari_dialogs():
        teamRocketBlocksLabel.place_forget()
        confrontButton.place_forget()
        safariCanvas.itemconfig(dialogBackground, state="normal")
        safariCanvas.itemconfig(dialogBox, state="normal")

        # get the dialogues:
        opponent_tuple = skyblockPuzzle.three_weirdos()

        curr_opponent_id = 0

        opponentNameLabel.configure(text="Safari Shenanigans")
        opponentNameLabel.place(x=50, y=410)
        opponentRiddleLabel.configure(text="Prepare for trouble, and make it double! We'll give you three statements. Figure out who stole your catch, before we run away!", wraplength=700, justify="left")
        opponentRiddleLabel.place(x=50, y=450)


        def safari_dialogs_continued():
            nonlocal curr_opponent_id
            if curr_opponent_id < 3:
                opponentNameLabel.configure(text=opponent_tuple[curr_opponent_id][0])
                opponentRiddleLabel.configure(text=opponent_tuple[curr_opponent_id][1], wraplength=700, justify="left")
                curr_opponent_id += 1
            else:
                # hide the dialog things
                dialogContinueButton.destroy()
                safariCanvas.itemconfig(dialogBackground, state="hidden")
                safariCanvas.itemconfig(dialogBox, state="hidden")
                opponentNameLabel.place_forget()
                opponentRiddleLabel.place_forget()

                # show the choice buttons!
                choice1Button = tk.Button(safariFrame, text=opponent_tuple[0][0], font="Helvetica 14", command=lambda: select_opponent(0))
                choice1Button.place(x=150, y=250, height=40, anchor="e")
                button_glow.bind_normal(choice1Button)
                choice2Button = tk.Button(safariFrame, text=opponent_tuple[1][0], font="Helvetica 14", command=lambda: select_opponent(1))
                choice2Button.place(x=150, y=350, height=40, anchor="e")
                button_glow.bind_normal(choice2Button)
                choice3Button = tk.Button(safariFrame, text=opponent_tuple[2][0], font="Helvetica 14", command=lambda: select_opponent(2))
                choice3Button.place(x=150, y=450, height=40, anchor="e")
                button_glow.bind_normal(choice3Button)

            def select_opponent(opponent):
                # hide the buttons
                choice1Button.destroy()
                choice2Button.destroy()
                choice3Button.destroy()


                def safari_leave():
                    # first, hide the stuff for the next time we get here
                    exitDialogButton.destroy()
                    safariCanvas.itemconfig(dialogBackground, state="hidden")
                    safariCanvas.itemconfig(dialogBox, state="hidden")
                    opponentNameLabel.place_forget()
                    opponentRiddleLabel.place_forget()

                    # switch frames
                    safariFrame.place_forget()
                    mainMapFrame.place(x=0, y=0, relwidth=1, relheight=1)


                # set up dialog box
                safariCanvas.itemconfig(dialogBackground, state="normal")
                safariCanvas.itemconfig(dialogBox, state="normal")

                exitDialogButton = tk.Button(safariFrame, text="Continue", font="Helvetica 21", command=safari_leave)
                button_glow.bind_normal(exitDialogButton)
                exitDialogButton.place(x=600, y=500, height=40)

                if opponent_tuple[opponent][2]: # true if correct!
                    pokeList = file_IO.fetch_list("../PokeList_v3.csv", False)
                    newPokemon = game_functions.catch_pokemon(playerData,pokeList[random.randint(1, 150)])
                    candy_awarded = game_functions.award_candy(playerData)

                    opponentNameLabel.configure(text="Team Rocket blasting off again!")
                    opponentRiddleLabel.configure(text=f"{opponent_tuple[opponent][0]} had your catch! You give Team Rocket the boot, gained {candy_awarded} candies, and added a pokemon to your team!"
                                                  + f"\n#{int(newPokemon[0])} {newPokemon[1]}, {newPokemon[2]} C.P.", wraplength=700, justify="left")
                else:
                    opponentNameLabel.configure(text="They got away...")
                    opponentRiddleLabel.configure(text=f"{opponent_tuple[opponent][0]} was not the one who stole your catch. Team rocket got away!", wraplength=700, justify="left")

                opponentNameLabel.place(x=50, y=410)
                opponentRiddleLabel.place(x=50, y=450)





        dialogContinueButton = tk.Button(safariFrame, text="Continue", font="Helvetica 21", command=safari_dialogs_continued)
        button_glow.bind_normal(dialogContinueButton)
        dialogContinueButton.place(x=600, y=500, height=40)









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
    safariButton = tk.Button(mainMapFrame, text="safari", activebackground="sky blue", relief="flat", command=safari_enter)
    safariButton.place(relx=0.2, rely=0.2, anchor="center")


    ##### generating the tutorial house frame
    helpHouseFrame = tk.Frame(gameWindow)
    # helpHouseFrame.place(x=0, y=0, relwidth=1, relheight=1)
    helpHouseCanvas = tk.Canvas(helpHouseFrame, width=800, height=600)
    helpHouseCanvas.pack(fill="both", expand=True)
    helpHouseEntryImage = tk.PhotoImage(file="../Images/tutorialHouseBackground.png")
    helpHouseCanvas.create_image(0, 0, image=helpHouseEntryImage, anchor="nw")
    helpHouseExitButton = tk.Button(helpHouseFrame, text="exit", font="Helvetica 21", command=tutorial_house_leave)
    helpHouseExitButton.place(relx=0.5, rely=0.9, anchor="center", height=40)


    #### generating the safari transition frame
    safariFrame = tk.Frame(gameWindow)
    safariCanvas = tk.Canvas(safariFrame, width=800, height=600)
    safariCanvas.pack(fill="both", expand=True)
    safariBackground = tk.PhotoImage(file="../Images/safariBackground.png")
    safariCanvas.create_image(0, 0, image=safariBackground, anchor="nw")

    teamRocketBlocksLabel = tk.Label(safariFrame, text="Team Rocket blocks the way!", font="Helvetica 21", fg="yellow", bg="brown", relief="raised")
    # teamRocketBlocksLabel.place(relx=0.5, rely=0.1, anchor="n")

    dialogBackgroundImage = tk.PhotoImage(file="../Images/safariBackgroundDialouge.png")
    dialogBackground = safariCanvas.create_image(0, 0, image=dialogBackgroundImage, anchor="nw")
    safariCanvas.itemconfig(dialogBackground, state="hidden")

    dialogBox = safariCanvas.create_rectangle(25, 400, 775, 550, fill="saddle brown", outline="yellow", width=6)
    safariCanvas.itemconfig(dialogBox, state="hidden")

    opponentNameLabel = tk.Label(safariFrame, text="", font="Helvetica 21", fg="yellow", bg="saddle brown")
    opponentRiddleLabel = tk.Label(safariFrame, text="", font="Helvetica 14", fg="yellow", bg="saddle brown")

    confrontButton = tk.Button(safariFrame, text="Confront!", font="Helvetica 21", command=safari_dialogs)
    # confrontButton.place(relx=0.5, rely=0.8, anchor="center", height=40)
    button_glow.bind_red(confrontButton)


    gameWindow.mainloop()
