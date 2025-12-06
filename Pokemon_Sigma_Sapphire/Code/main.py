'''
import keyboard
import os
import time
import msvcrt
'''
import game









#Change read file path as needed for your file system
#global read_path
read_path = "Pokemon_Sigma_Sapphire\\PokeList_v3.csv"

'''
run = True
men = True
key = ''
'''



'''    moved into its own file
def fetch_list(file_path, show_first = False):
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

'''



'''
def login():
    username = input("Username: ")
    print()
    password = input("Password: ")


def create_account():
    pass


def draw_line(char="-"):
    print(f"{char*30}")#------------------------------")

def console_resize(x, y, char):
    #os.system('cls')
    clear()
    inp = input("Do you need to resize console? Type: (Y/n) > ").lower()

    if inp == "y":
        #os.system('cls')
        clear()

        print("For this next step, drag the borders of your console to closely match the block of text without touching")
        print("Once you are finished, press enter to continue")

        inp = input("Are you ready to move on to the next step? Type: (Y/n) > ").lower()
        if inp == "y":
            #os.system('cls')
            clear()
            line = char * x
            for i in range(y):
                print(line)

            inp = input()

            #get_key()
            #if key == ' ':
            #    pass


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

'''


'''
def menu():
    #global key
    #os.system('cls') #This is the command for windows os.system('clear') for mac
    clear()
    draw_line()
    print("1. Play")
    print("2. Login")
    print("3. Create Account")
    print("4. Quit Game")
    draw_line()

    #get_key()
    key = input(">")
    if key not in ['1', '2', '3', '4']:
        #key = input(">")
        menu()

    if key == '4':
        quit()
    elif key == '1':
        game()
    elif key == '2':
        login()
    elif key == '3':
        create_account()  
    else:
        print("You have severly broken the program")
        #quit()




def pause():
    pass

def draw_frame(top_bar, game_space, bottom_bar):
    clear()
    for line in range(top_bar):
        print(line)

    for line in range(game_space):
        print(line)
    
    for line in range(bottom_bar):
        print(line)

'''


#Total screen space as of now (we can change it)  (x,y) = (100, 40)
#Makes a square because of line spacing. Basically distance between chars on the y axis are longer than the x
'''
game board:
1====================================================================================================         100 ='s
2  Player_name                                  stuff                                     p - pause 
3====================================================================================================
4                                                                                                    
5                                                                                                   
6                                                                                                   
7                                                                                                   
8                                                                                                   
9                                                                                                   
0                                                                                                   
1                                                                                                   
2                                                                                                   
3                                                                                                   
4                                                                                                   
5                                                                                                                                          Actual game stuff
6                                                                                                   
7                                                                                                   
8                                                                                                   
9                                                                                                   
0                                                                                                   
1                                                                                                   
2                                                                                                   
3                                                                                                   
4                                                                                                   
5                                                                                                   
6                                                                                                   
7                                                                                                   
8                                                                                                   
9                                                                                                   
0====================================================================================================
1                                            Example
2   
3
4   Option 1.                    Option 5.        
5   Option 2.                    Option 6.
6   Option 3.                    Option 7.
7   Option 4.                    Option 8.
8 
9
0====================================================================================================







Hmmm maybe we should use curses






'''

'''
def game(key=''):
    clear()
    print("Inside of the game")
    draw_frame()
    key = input(">")
    if key == 'q':
        quit()
    #elif men == True:
    #    menu()
    elif key == 'p':
        pause()
    else:
        pass
'''

first = True

'''
def get_key():
    global key
    #key = keyboard.read_key()
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            return
'''

'''

def title_screen():
    draw_line()
    draw_line("*")
    print()
    print("Welcome to Pokemon Sigma Sapphire!")
    print("-----Press Enter to Continue-----")
    print()
    draw_line("*")
    draw_line()
    key = input()
    #get_key()
    #if key == 'space':
    #    return
'''





#player_file_locations = ["player1.json", "player2.json", "player3.json", "player4.json"]

def main():

    pass
    #main_menu.run_menu()


    




if __name__ == "__main__":
    main()