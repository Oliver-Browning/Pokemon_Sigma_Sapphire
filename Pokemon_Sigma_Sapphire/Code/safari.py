import tkinter as tk
import skyblockPuzzle



def run_safari():


    safari_window = tk.Tk()

    safari_window.geometry("800x600")
    safari_window.resizable(False, False)
    safari_window.title("Safari")


    weirdo_tuple = skyblockPuzzle.three_weirdos()


    #weirdo_1 = weirdo_tuple[0]

    weirdo_1_name = weirdo_tuple[0][0]
    weirdo_1_dialogue = weirdo_tuple[0][1]

    weirdo_2_name = weirdo_tuple[1][0]
    weirdo_2_dialogue = weirdo_tuple[1][1]

    weirdo_3_name = weirdo_tuple[2][0]
    weirdo_3_dialogue = weirdo_tuple[2][1]

    game_won = False

    '''
    def option_selected(option):
        global game_won

        if option == 1:
            game_won = weirdo_tuple[0][2]
            print(game_won)
        elif option == 2:
            game_won = weirdo_tuple[1][2]
            print(game_won)
        elif option == 3:
             game_won = weirdo_tuple[2][2]
             print(game_won)
        else:
            print("Something went wrong between button press and this function")
        print(game_won)
        '''

    def option_1_selected():
        game_won = weirdo_tuple[0][2]
        print(game_won)

    def option_2_selected():
        game_won = weirdo_tuple[1][2]
        print(game_won)

    def option_3_selected():
        game_won = weirdo_tuple[2][2]
        print(game_won)

            


    option_1 = tk.Button(safari_window, text = weirdo_1_name, command = option_1_selected)
    option_2 = tk.Button(safari_window, text = weirdo_2_name, command = option_2_selected)
    option_3 = tk.Button(safari_window, text = weirdo_3_name, command = option_3_selected)
    #option_4 = tk.Button(safari_window, text = game_won)

    #T = tk.Text(safari_window, height = "5", width = "10")
    lab = tk.Label(safari_window, text=game_won)

    option_1.pack()
    option_2.pack()
    option_3.pack()
    lab.pack()

    #   139,Kabuto,170,270

    safari_window.mainloop()

if __name__ == "__main__":
    run_safari()

    #print(help(tk.Button()))