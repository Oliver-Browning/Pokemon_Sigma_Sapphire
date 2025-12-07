import tkinter as tk




def run_safari():


    safari_window = tk.Tk()

    safari_window.geometry("800x600")
    safari_window.resizable(False, False)
    safari_window.title("Safari")


    def option_selected(option):
        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        else:
            print("Something went wrong between button press and this function")




    option_1 = tk.Button(safari_window, text = "Option 1", command = option_selected(1))
    option_2 = tk.Button(safari_window, text = "Option 2", command = option_selected(2))
    option_3 = tk.Button(safari_window, text = "Option 3", command = option_selected(3))

    option_1.pack()
    option_2.pack()
    option_3.pack()





    safari_window.mainloop()

if __name__ == "__main__":
    #run_safari()
    print(help(tk.Button()))