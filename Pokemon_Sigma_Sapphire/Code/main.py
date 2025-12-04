import keyboard
import os




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
    pass

def create_account():
    pass

def draw():
    print("------------------------------")

def menu():
    #global key
    os.system('cls') #This is the command for windows os.system('clear') for mac
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
    key = keyboard.read_key()


def main():
    while True:
        #print(f"In main loop{__name__}")
        global first
        if first:
            game()
            first = False
        else:
            #key_input = keyboard.read_key()
            get_key()
            game()

        
        

        #poke_list = fetch_pokemon_list(True)
        #print(poke_list[0:2])





if __name__ == "__main__":
    main()