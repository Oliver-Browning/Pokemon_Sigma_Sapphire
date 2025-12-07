import minigame
import time

button_pressed = False

while True:

    minigame.start_minigame(button_pressed)
    inp = input("Press enter to throw pokeball")
    if inp == "":
        button_pressed
        


