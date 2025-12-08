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

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import file_IO
import game_functions
import button_glow
import skyblockPuzzle
import random
import main_menu

def run_game(playerData, all_player_data):
    """
    Takes in playerData (dict) and all_player_data (dict)
    Launches and runs the main Sigma Sapphire game window.
    This function initializes the Tkinter window, loads all map locations,
    Creates UI frames (main map, arena, Pokemon Center, Instructions House, and the Safari)
    """

    # the usual general setup
    gameWindow = tk.Tk()
    gameWindow.title("Pokemon Sigma Sapphire: " + playerData["name"])
    gameWindow.resizable(False, False)
    gameWindow.geometry("800x600")


    # this function handles entering the tutorial house!
    def tutorial_house_enter():
        """
        This function handles the user entering the instructions home page.
        """
        mainMapFrame.place_forget()
        helpHouseFrame.place(x=0, y=0, relwidth=1, relheight=1)

    def tutorial_house_leave():
        """
        This function handles the user leaving the instructions home page.
        """
        helpHouseFrame.place_forget()
        mainMapFrame.place(x=0, y=0, relwidth=1, relheight=1)

    # this function handles entering the safari!


    def arena_enter():
        """
        This function handles the user entering the arena home page.
        """
        mainMapFrame.place_forget()
        arenaFrame.place(x=0, y=0, relwidth=1, relheight=1)

        # update dropdown selector!
        # updating the selection dropdown!
        pokeNameList = [pokemon[1] for pokemon in playerData["pokemon"]]
        arenaSelector.configure(values=pokeNameList)


    def arena_leave():
        """
        This function handles the user leaving the arena home page.
        """
        arenaFrame.place_forget()
        mainMapFrame.place(x=0, y=0, relwidth=1, relheight=1)

    def fake_full_enter():
        """
        This function is called when you press the continue button in the arena.
        It hides the arena background and takes you to a screen that says to buy 
        the full version.
        """
        arenaFrame.place_forget()
        fullVersionFrame.place(x=0, y=0, relwidth=1, relheight=1)

    def fake_full_leave():
        """
        Hides the buy the full version screen and takes you back to the arena.
        """
        fullVersionFrame.place_forget()
        arenaFrame.place(x=0, y=0, relwidth=1, relheight=1)


    def update_pokemonCenterLister():
        '''
        Updates the Pokemon list displayed inside the pokemon center.
        This function rewrites the list of pokemon currently owned 
        by the player, including their Pokedex ID, name, level, and combat Power
        '''
        pokemonCenterLister.configure(state="normal")  # enable editing, since it's normally disabled
        pokemonCenterLister.delete("1.0", tk.END)
        toShow = ""
        for pokemon in playerData["pokemon"]:
            toShow += f"#{pokemon[0]}: {pokemon[1]}\n"  # ID and Name
            toShow += f"Level: {pokemon[3]}\n"  # Level
            toShow += f"Combat Power: {pokemon[2]}\n"  # Combat Power
            toShow += "\n"  # blank line between pokemon!
        pokemonCenterLister.insert("1.0", toShow)
        pokemonCenterLister.configure(state="disabled")  # done, so we can keep the player from editing it!

    def pokemonCenter_enter():
        '''
        Handles transition into the pokemon center.
        It hides the main map frame and displays the Pokemon Center frame.
        It then refreshes the Pokemon list and candy count for the player.
        '''
        mainMapFrame.place_forget()
        pokemonCenterFrame.place(x=0, y=0, relwidth=1, relheight=1)

        # updating the selection dropdown!
        pokeNameList = [pokemon[1] for pokemon in playerData["pokemon"]]
        pokemonCenterSelector.configure(values=pokeNameList)

        update_pokemonCenterLister()


    def pokemonCenter_leave():
        '''
        Handles the transition out of the Pokemon center.
        Hides the Pokemon Center frame and returns the player to the main map.
        '''
        pokemonCenterFrame.place_forget()
        mainMapFrame.place(x=0, y=0, relwidth=1, relheight=1)

    def invoke_feeding():
        '''
        Feeds candies to a selected pokemon to increase its level.
        This function reads the user's input from the selection box, 
        calls the leveling function, updates the player's candy count 
        on screen, and then refreshes the pokemon list display to
        reflect the new stats.
        '''
        # this is its own function because we need to update the GUI as well as do the internal updates!
        game_functions.level_pokemon(pokemonCenterSelector.get(),playerData)
        pokemonCenterCandyCountLabel.configure(text = str(playerData["candies"]))   #We changed this to text = and it WORKS!

        update_pokemonCenterLister()


    def safari_enter():
        """
        Handles the transition into the Safari map.
        Hides the main map frame and displays the safari frame. 
        This initializes the encounter by placing the confrontation 
        button and introductory text.
        """
        mainMapFrame.place_forget()
        safariFrame.place(x=0, y=0, relwidth=1, relheight=1)

        # show the initial confrontation things!
        confrontButton.place(relx=0.5, rely=0.8, anchor="center", height=40)
        teamRocketBlocksLabel.place(relx=0.5, rely=0.1, anchor="n")

        # safari.run_safari(playerData)


    def safari_dialogs():
        """
        Begins the safari dialogue sequence with Team Rocket.
        This function displays the dialog UI elements, 
        retrieves the three-riddle encounter from skyblockPuzzle, 
        and cycles through each statement. After the dialogue, 
        the function presents the player with three suspects to choose from.
        """

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
            """
            This function continues the dialogue sequence for the Safari game, 
            where it displays each of the three riddle statements one at a time. 
            After the final statement, it hides the dialogue box and displays 
            three selectable opponent buttons for the player to choose from.
            """
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
                choice1Button.place(x=150, y=280, height=40, anchor="e")
                button_glow.bind_normal(choice1Button)
                choice2Button = tk.Button(safariFrame, text=opponent_tuple[1][0], font="Helvetica 14", command=lambda: select_opponent(1))
                choice2Button.place(x=150, y=370, height=40, anchor="e")
                button_glow.bind_normal(choice2Button)
                choice3Button = tk.Button(safariFrame, text=opponent_tuple[2][0], font="Helvetica 14", command=lambda: select_opponent(2))
                choice3Button.place(x=150, y=460, height=40, anchor="e")
                button_glow.bind_normal(choice3Button)

            def select_opponent(opponent):
                """
                Takes in an integer of either 0, 1, or 2 for which 
                opponent was selected. Is called by the choice 
                buttons next to each of the 3 opponents in the minigame. 
                Removes all of the opponent choice buttons from the 
                screen. Defines the safari_leave() function, and 
                sets up the win/lose dialogue box. Makes a continue 
                button that calls safari_leave(). Checks to see if the 
                player won the game, and if so, reward the player with 
                a new pokemon and candy, and display the win dialogue. 
                If they didn't win, display the lose dialogue. Returns nothing.
                """
                choice1Button.destroy()
                choice2Button.destroy()
                choice3Button.destroy()


                def safari_leave():
                    """
                    Takes in no arguments. It is called when you click 
                    the continue button after playing the minigame. 
                    Removes and hides all safari related things like the 
                    opponents and their dialogue. It hides the safari 
                    window and shows the main town area. Returns nothing.
                    """
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
                    nonlocal playerData
                    newPokemon, playerData = game_functions.catch_pokemon(playerData,pokeList[random.randint(1, 150)])
                    candy_awarded = game_functions.award_candy(playerData)


                    # save the player data
                    game_functions.save_player_data(playerData, all_player_data, candy_awarded)

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
    arenaButton = tk.Button(mainMapFrame, image=arenaImage, activebackground="sky blue", relief="flat", command=arena_enter)
    arenaButton.place(x=640, y=430, anchor="center", width=192, height=130)

    #pokemon center
    pokemonCenterImage = tk.PhotoImage(file="../Images/pokemon_Center.png")
    pokemonCenterButton = tk.Button(mainMapFrame, image=pokemonCenterImage, activebackground="sky blue", relief="flat", command=pokemonCenter_enter)
    pokemonCenterButton.place(x=624, y=208, anchor="center", width=158, height=128)

    # safari
    safariButtonImage = tk.PhotoImage(file="../Images/safari_Truck.png")
    safariButton = tk.Button(mainMapFrame, image=safariButtonImage, relief="flat", command=safari_enter)
    safariButton.place(x=121, y=158, width=61, height=35, anchor="nw")


    #Return to main menu button
    stonePathMenuButtonImage = tk.PhotoImage(file="../Images/exit_arrow.png")
    stonePathMenuButton = tk.Button(mainMapFrame, image=stonePathMenuButtonImage, bg="#685A5B", command=gameWindow.destroy)
    stonePathMenuButton.place(x=384, y=564, width=32, height=32, anchor="nw")


    # ACTIVE POKEMON FUNCTION
    def invoke_active():
        """
        Takes in no arguments. It is called when you press the select 
        active pokemon button. It runs the active_pokemon function 
        and passes it the name of the pokemon that the user selected 
        in the user interface, as well as the player data. It then 
        configures the label to display the name of the active pokemon. 
        Returns nothing.
        """

        game_functions.active_pokemon(arenaSelector.get(), playerData)

        arenaActiveLabel.configure(text=str(playerData["active pokemon"][1]))
        arenaActiveLevelLabel.configure(text=("Level " + str(playerData["active pokemon"][3])))
        arenaActiveComPowerLabel.configure(text=f"Combat Power: {playerData["active pokemon"][2]}")
        arenaActiveIDLabel.configure(text=f"ID: #{playerData['active pokemon'][0]}")

    ##### Generating the arena frame
    arenaFrame = tk.Frame(gameWindow)
    arenaCanvas = tk.Canvas(arenaFrame, width=800, height=600)
    arenaCanvas.pack(fill="both", expand=True)
    arenaEntryImage = tk.PhotoImage(file="../Images/arena_bg.png")
    arenaCanvas.create_image(0, 0, image=arenaEntryImage, anchor="nw")
    arenaExitButton = tk.Button(arenaFrame, text="Exit", font="Helvetica 21", command=arena_leave)
    arenaExitButton.place(relx=0.465, rely=0.95, anchor="e", height=35)
    button_glow.bind_normal(arenaExitButton)
    arenaFightButton = tk.Button(arenaFrame, text="Fight!", font="Helvetica 21", command=fake_full_enter)
    arenaFightButton.place(relx=0.515, rely=0.95, anchor="w", height=35)
    button_glow.bind_red(arenaFightButton)

    ## Selecting an active pokemon
    arenaActiveButton = tk.Button(arenaFrame, text="Select as Active", font="Helvatica 21", command=invoke_active)
    arenaActiveButton.place(relx=0.7, rely=0.1125, anchor="center", height=40)  # Change the location of this to be correct
    button_glow.bind_normal(arenaActiveButton)

    # Selector box
    pokeNameList = [pokemon[1] for pokemon in playerData["pokemon"]]
    arenaSelector = ttk.Combobox(arenaFrame, font="Helvetica 21", values=pokeNameList, state="readonly")
    arenaSelector.place(relx=0.35, rely=0.1125, relwidth=0.4, anchor="center", height=40)

    arenaActiveLabel = tk.Label(arenaFrame, text=playerData["active pokemon"][1], font="Helvetica 28", fg="yellow", bg="#2BA4D9", anchor="w")
    arenaActiveLabel.place(x=240, rely=0.2075, anchor="w", width=300)
    arenaActiveLevelLabel = tk.Label(arenaFrame, text=("Level " + str(playerData["active pokemon"][3])), font="Helvetica 28", fg="yellow", bg="#2BA4D9", anchor="e")
    arenaActiveLevelLabel.place(x=690, rely=0.2075, anchor="e", width=150)
    arenaActiveComPowerLabel = tk.Label(arenaFrame, text=f"Combat Power: {playerData["active pokemon"][2]}", font="Helvetica 14", fg="yellow", bg="#2BA4D9", anchor="w")
    arenaActiveComPowerLabel.place(x=240, rely=0.27, anchor="w", width=300)
    arenaActiveIDLabel = tk.Label(arenaFrame, text=f"ID: #{playerData['active pokemon'][0]}", font="Helvetica 14", fg="yellow", bg="#2BA4D9", anchor="e")
    arenaActiveIDLabel.place(x=690, rely=0.27, anchor="e", width=150)

    # literally just a frame to fake tease the full game lol
    fullVersionFrame = tk.Frame(gameWindow)
    fullVersionCanvas = tk.Canvas(fullVersionFrame, width=800, height=600)
    fullVersionCanvas.pack(fill="both", expand=True)
    fullVersionBackgroundImage = tk.PhotoImage(file="../Images/fullVersion_bg.png")
    fullVersionCanvas.create_image(0, 0, image=fullVersionBackgroundImage, anchor="nw")
    fullVersionCanvasContinueButton = tk.Button(fullVersionFrame, text="Continue", font="Helvetica 21", command=fake_full_leave)
    fullVersionCanvasContinueButton.place(relx=0.5, rely=0.9425, anchor="center", height=40)
    button_glow.bind_normal(fullVersionCanvasContinueButton)



    ##### Generating pokemon center frame
    pokemonCenterFrame = tk.Frame(gameWindow) #pokemonCenter
    pokemonCenterCanvas = tk.Canvas(pokemonCenterFrame, width=800, height=600)
    pokemonCenterCanvas.pack(fill="both", expand=True)
    pokemonCenterBackgroundImage = tk.PhotoImage(file="../Images/pokemon_center_bg.png")
    pokemonCenterCanvas.create_image(0, 0, image=pokemonCenterBackgroundImage, anchor="nw")
    pokemonCenterExitButton = tk.Button(pokemonCenterFrame, text="exit", font="Helvetica 21", command=pokemonCenter_leave)
    button_glow.bind_normal(pokemonCenterExitButton)
    pokemonCenterExitButton.place(relx=0.5, rely=0.9425, anchor="center", height=40)

    pokemonCenterLister = scrolledtext.ScrolledText(pokemonCenterFrame, wrap=tk.WORD, font="Helvetica 14", fg="yellow", bg="#2BA4D9")
    pokemonCenterLister.place(relx=0.5, rely=0.425, anchor="center", width=575, height=380)
    pokemonCenterLister.configure(state="disabled") # done, so we can keep the player from editing it!


    # feeding related stuff
    # Selector box
    pokeNameList = [pokemon[1] for pokemon in playerData["pokemon"]]
    pokemonCenterSelector = ttk.Combobox(pokemonCenterFrame, font="Helvetica 21", values=pokeNameList, state="readonly")
    pokemonCenterSelector.place(relx=0.5, rely=0.8, relwidth=0.4, anchor="center", height=40)

    #Feed Button
    pokemonCenterFeedButton = tk.Button(pokemonCenterFrame, text="Feed", font="Helvatica 21", command=invoke_feeding)
    pokemonCenterFeedButton.place(relx=0.775, rely=0.8, relwidth=0.125, anchor="center", height=40)
    button_glow.bind_normal(pokemonCenterFeedButton)

    #Candy count label with actual count
    pokemonCenterCandyCountLabel = tk.Label(pokemonCenterFrame, text=playerData["candies"], font="Helvetica 28", fg="yellow", bg="#2BA4D9")
    pokemonCenterCandyCountLabel.place(relx=0.23, rely=0.82, anchor="center", width=75)
    
    pokemonCenterCandyCandyLabel = tk.Label(pokemonCenterFrame, text="Candy:", font="Helvetica 14", fg="yellow", bg="#2BA4D9")
    pokemonCenterCandyCandyLabel.place(relx=0.23, rely=0.77, anchor="center", width=75)



    ##### generating the tutorial house frame
    helpHouseFrame = tk.Frame(gameWindow)
    # helpHouseFrame.place(x=0, y=0, relwidth=1, relheight=1)
    helpHouseCanvas = tk.Canvas(helpHouseFrame, width=800, height=600)
    helpHouseCanvas.pack(fill="both", expand=True)
    helpHouseEntryImage = tk.PhotoImage(file="../Images/tutorialHouseBackground.png")
    helpHouseCanvas.create_image(0, 0, image=helpHouseEntryImage, anchor="nw")
    helpHouseExitButton = tk.Button(helpHouseFrame, text="exit", font="Helvetica 21", command=tutorial_house_leave)
    button_glow.bind_normal(helpHouseExitButton)
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


if __name__ == "__main__":
    run_game(file_IO.fetch_json("../player_data/playerData.json")["Noam"], file_IO.fetch_json("../player_data/playerData.json"))
