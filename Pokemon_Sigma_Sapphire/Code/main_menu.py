import tkinter as tk
import file_IO
import button_glow
import os

def run_menu():
    '''
    This function invokes the main menu screen, and all associated functionality.
    It returns the selected player's name, or if "Quit" is pressed, boolean False.
    '''

    # os.system('start ../Audio/"Pokemon Theme (8 Bit Raxlen Slice Chiptune Remix) [DeTJQf57wwQ].mp3"')

    # get the last played player - that will be the default
    player = file_IO.fetch_json("../player_data/last_save_used.json")["lastPlayed"]



    # generate the main window
    menuWindow = tk.Tk()
    menuWindow.geometry("800x600")
    menuWindow.resizable(False, False)
    menuWindow.title("Pokemon Sigma Sapphire")

    # main background image
    background = tk.PhotoImage(file="../images/mainMenu_Background.png")

    # actaully putting it on the canvas so it renders
    backCanvas = tk.Canvas(menuWindow, width=800, height=600)
    backCanvas.pack(fill="both", expand=True)
    backCanvas.create_image(0, 0, image=background, anchor="nw")

    # stuff relating to manipulating save data
    saveChangeBackground = tk.PhotoImage(file="../images/mainMenu_SAVECHANGE_Background.png")
    saveChangeBackgroundImage = backCanvas.create_image(447, 57, image=saveChangeBackground, anchor="nw")
    backCanvas.itemconfig(saveChangeBackgroundImage, state='hidden')


    # player selected - return with their name!
    def player_selected():
        menuWindow.destroy()


    def show_save_change_things():
        backCanvas.itemconfig(saveChangeBackgroundImage, state='normal')
        continueButton.configure(state='disabled')
        savesButton.configure(state='disabled')

        # save change menu items
        p1Select.place(x=535, y=200, anchor="center", height=40)
        p2Select.place(x=535, y=300, anchor="center", height=40)
        p3Select.place(x=535, y=400, anchor="center", height=40)
        p4Select.place(x=535, y=500, anchor="center", height=40)
        p1Reset.place(x=660, y=200, anchor="center", height=40)
        p2Reset.place(x=660, y=300, anchor="center", height=40)
        p3Reset.place(x=660, y=400, anchor="center", height=40)
        p4Reset.place(x=660, y=500, anchor="center", height=40)

        p1Label.place(x=600, y=150, anchor="center")
        p2Label.place(x=600, y=250, anchor="center")
        p3Label.place(x=600, y=350, anchor="center")
        p4Label.place(x=600, y=450, anchor="center")

    def hide_save_change_things(playerName):
        nonlocal player
        player = playerName

        backCanvas.itemconfig(saveChangeBackgroundImage, state='hidden')
        continueButton.configure(state='normal')
        savesButton.configure(state='normal')
        playerSelectedLabel.configure(text=("  Player: " + playerName + "  ")) # don't forget to show who's playing!

        # save change menu items
        p1Select.place_forget()
        p2Select.place_forget()
        p3Select.place_forget()
        p4Select.place_forget()
        p1Reset.place_forget()
        p2Reset.place_forget()
        p3Reset.place_forget()
        p4Reset.place_forget()

        p1Label.place_forget()
        p2Label.place_forget()
        p3Label.place_forget()
        p4Label.place_forget()



    def reset_save_file(playerName):
        nonlocal players
        players[playerName]["level"] = 1
        players[playerName]["candies"] = 0
        players[playerName]["pokemon"] = []


    def quit_menu():
        nonlocal player
        player = False
        menuWindow.destroy()


    # labels with player data
    players = file_IO.fetch_json("../player_data/playerData.json")
    playerNames = []
    for name in players:
        playerNames.append(name)
    p1Label = tk.Label(menuWindow, text=(
                                         playerNames[0] + ": Level " + str(players[playerNames[0]]["level"])
                                         + ", Candies: " + str(players[playerNames[0]]["candies"])
                                         ), font="Ariel 13 bold", fg="yellow", bg="#2BA4D9")

    p2Label = tk.Label(menuWindow, text=(
                                         playerNames[1] + ": Level " + str(players[playerNames[1]]["level"])
                                         + ", Candies: " + str(players[playerNames[1]]["candies"])
                                         ), font="Ariel 13 bold", fg="yellow", bg="#2BA4D9")

    p3Label = tk.Label(menuWindow, text=(
                                         playerNames[2] + ": Level " + str(players[playerNames[2]]["level"])
                                         + ", Candies: " + str(players[playerNames[2]]["candies"])
                                         ), font="Ariel 13 bold", fg="yellow", bg="#2BA4D9")

    p4Label = tk.Label(menuWindow, text=(
                                         playerNames[3] + ": Level " + str(players[playerNames[3]]["level"])
                                         + ", Candies: " + str(players[playerNames[3]]["candies"])
                                         ), font="Ariel 13 bold", fg="yellow", bg="#2BA4D9")


    # buttons for manipulating
    p1Select = tk.Button(menuWindow, text="Select", font="Helvetica 21", command= lambda: hide_save_change_things(playerNames[0]))
    p2Select = tk.Button(menuWindow, text="Select", font="Helvetica 21", command= lambda: hide_save_change_things(playerNames[1]))
    p3Select = tk.Button(menuWindow, text="Select", font="Helvetica 21", command= lambda: hide_save_change_things(playerNames[2]))
    p4Select = tk.Button(menuWindow, text="Select", font="Helvetica 21", command= lambda: hide_save_change_things(playerNames[3]))
    p1Reset = tk.Button(menuWindow, text="Reset", font="Helvetica 21")
    p2Reset = tk.Button(menuWindow, text="Reset", font="Helvetica 21")
    p3Reset = tk.Button(menuWindow, text="Reset", font="Helvetica 21")
    p4Reset = tk.Button(menuWindow, text="Reset", font="Helvetica 21")


    # generating the MAIN menu items

    playerSelectedLabel = tk.Label(menuWindow, text=("  Player: " + player + "  "), font="Ariel 13 bold", fg="white", bg="dark blue")
    playerSelectedLabel.place(x=165, y=432, anchor="center")

    continueButton = tk.Button(menuWindow, text="Continue", font="Helvetica 21", command=player_selected)
    continueButton.place(x=165, y=470, anchor="center", height=40)

    savesButton = tk.Button(menuWindow, text="Saves", font="Helvetica 21", command=show_save_change_things)
    savesButton.place(x=165, y=515, anchor="center", height=40)

    quitButton = tk.Button(menuWindow, text="Quit", font="Helvetica 21", command=quit_menu)
    quitButton.place(x=165, y=560, anchor="center", height=40)


    # setting color binding!
    button_glow.bind_normal(continueButton)
    button_glow.bind_normal(savesButton)
    button_glow.bind_red(quitButton)

    button_glow.bind_normal(p1Select)
    button_glow.bind_normal(p2Select)
    button_glow.bind_normal(p3Select)
    button_glow.bind_normal(p4Select)

    button_glow.bind_red(p1Reset)
    button_glow.bind_red(p2Reset)
    button_glow.bind_red(p3Reset)
    button_glow.bind_red(p4Reset)



    menuWindow.mainloop()

    return player

if __name__ == "__main__":
    run_menu()