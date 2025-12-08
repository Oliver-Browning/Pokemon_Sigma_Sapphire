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

# the following two functions handle changing the button color when hovered over!
def button_on_enter(caller):
    '''
    turns button blue on hover
    '''
    caller.widget['background'] = 'sky blue'

def button_on_leave(caller):
    '''
    returns button to normal upon end of hover
    '''
    caller.widget['background'] = 'SystemButtonFace'

# the following handles making the reset butons red when hovered over!
def reset_on_enter(caller):
    '''
    turns button red on hover
    '''
    caller.widget['background'] = 'OrangeRed'

# binds buttons to blue!
def bind_normal(caller):
    '''
    binds buttons to blue upon hover
    '''
    caller.bind("<Enter>", button_on_enter)
    caller.bind("<Leave>", button_on_leave)

# binds buttons to red!
def bind_red(caller):
    '''
    binds buttons to blue upon hover
    '''
    caller.bind("<Enter>", reset_on_enter)
    caller.bind("<Leave>", button_on_leave)