import keyboard
import os
import time
import msvcrt


#Change read file path as needed for your file system
#global read_path
read_path = "Pokemon_Sigma_Sapphire\\PokeList_v3.csv"
run = True
men = True
key = ''


def fetch_pokemon_list(show_first = False):
    """
    Reads PokeListv3.csv into a variable.
    show_first is a boolean that controls whether or not 
    the first line of the csv will be read to poke_list
    """
    with open(read_path, "r") as reading:
        lines = reading.readlines()
        line_list = []

        for line in lines:
            line_list.append(line.strip())

        if show_first == False:
            line_list = line_list[1:]

    return line_list


def login():
    username = input("Username: ")
    print()
    password = input("Password: ")


def create_account():
    pass


def draw(char="-"):
    print(f"{char*30}")#------------------------------")

def console_resize(x, y, char):
    #os.system('cls')
    clear()
    inp = input("Do you need to resize console? Type: (Y/n) > ").lower()

    if inp == "y":
        #os.system('cls')
        clear()

        print("For this next step, drag the borders of your console to closely match the block of text without touching")
        print("Once you are finished, press space to continue")

        inp = input("Are you ready to move on to the next step? Type: (Y/n) > ").lower()
        if inp == "y":
            #os.system('cls')
            clear()
            line = char * x
            for i in range(y):
                print(line)
        
            get_key()
            if key == ' ':
                pass


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')





def menu():
    #global key
    #os.system('cls') #This is the command for windows os.system('clear') for mac
    clear()
    draw()
    print("1. Play")
    print("2. Login")
    print("3. Create Account")
    print("4. Quit Game")
    draw()

    get_key()

    if key == '4':
        quit()
    elif key == '1':
        pass
    elif key == '2':
        login()
    elif key == '3':
        create_account()  
    else:
        pass




def pause():
    pass


def game(key=''):
    if key == 'q':
        quit()
    elif men == True:
        menu()
    elif key == 'p':
        pause()
    else:
        pass


first = True


def get_key():
    global key
    #key = keyboard.read_key()
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            return
    


def title_screen():
    draw()
    draw("*")
    print()
    print("Welcome to Pokemon Sigma Sapphire!")
    print("-----Press Space to Continue-----")
    print()
    draw("*")
    draw()
    get_key()
    if key == 'space':
        return


def main():
    #os.system('cls') #Maybe change into its own function where we can check if the system is a mac, and if so change the clear command to the mac one
    clear()
    while True:
        #print(f"In main loop{__name__}")
        global first
        if first:   #If this is the first time running the game, display the title screen
            title_screen()
            console_resize(100, 40, "#")
            game()
            first = False
        else:   #If not the first time running the game dont display the title screen
            #key_input = keyboard.read_key()
            get_key()
            game()


if __name__ == "__main__":
    main()