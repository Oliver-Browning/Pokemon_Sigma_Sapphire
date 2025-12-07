import tkinter as tk
#import skyBlockPuzzle



def run_safari():


    safari_window = tk.Tk()

    safari_window.geometry("800x600")
    safari_window.resizable(False, False)
    safari_window.title("Safari")


    weirdo_tuple = skyBlockPuzzle.three_weirdos()


    #weirdo_1 = weirdo_tuple[0]

    weirdo_1_name = weirdo_tuple[0][0]
    weirdo_1_dialogue = weirdo_tuple[0][1]

    weirdo_2_name = weirdo_tuple[1][0]
    weirdo_2_dialogue = weirdo_tuple[1][1]

    weirdo_3_name = weirdo_tuple[2][0]
    weirdo_3_dialogue = weirdo_tuple[2][1]

    game_won = False


    def option_selected(option):
        global game_won
        if option == 1:
                game_won = weirdo_tuple[0][2]
        elif option == 2:
            game_won = weirdo_tuple[1][2]
        elif option == 3:
             game_won = weirdo_tuple[2][2]
        else:
            print("Something went wrong between button press and this function")

    option_1 = tk.Button(safari_window, text = weirdo_1_name, command = option_selected(1))
    option_2 = tk.Button(safari_window, text = weirdo_2_name, command = option_selected(2))
    option_3 = tk.Button(safari_window, text = weirdo_3_name, command = option_selected(3))

    option_1.pack()
    option_2.pack()
    option_3.pack()


    safari_window.mainloop()

if __name__ == "__main__":
    run_safari()
    #print(help(tk.Button()))