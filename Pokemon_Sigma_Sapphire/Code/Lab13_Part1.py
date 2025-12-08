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

# FUNCTION STUBS

# imports
import random
import json
import tkinter as tk
import os


def fetch_list(file_path, show_first = True):
    """
    Takes a string file path file_path, and a boolean show_first of as arguments.
    Opens file, and reads into a list called line_list.
    If show_first is False, the first line (header) will 
    not be read into the list. Returns list.
    """
    pass


def push_list(file_path, line_list, mode="w"):
    """
    Takes a string file path file_path, a list of data called line_list
    and a string mode for the open mode. Opens/creates file and writes
    the data to the file in the mode specified. For debugging, returns
    boolean False if there was an error.
    """
    pass


def fetch_json(file_path):
    """
    Takes in json file_path, converts to dictionary, and returns it
    """
    pass


def push_json(file_path, dictionary, mode):
    """
    Takes in dictionary, converts it into json, then attemps to write it
    to a file, returning false if the process fails
    """
    pass

def award_candy():
    """
    Takes in no arguments. Generates a weighted random integer
    either 3, 5, or 10 and returns it to determine amount of candy awarded.
    """
    pass


def catch_pokemon(current_player_data, csvString):
    """
    Takes in arguments of current_player_data & the csvString of the pokemon caught. Adds the pokemon 
    (as identified by the csvString) into the "pokemon" list of current_player_data while properly generating
    said pokemon's combat power. At a high level, this adds a pokemon to current_player's pokemon list.
    """
    pass


def run_game(playerData):
    """
    Runs game for the player (determined by playerData) and renders objects and graphics
    """
    pass


def run_menu():
    '''
    This function invokes the main menu screen, and all associated functionality.
    It returns the selected player's name, or if "Quit" is pressed, boolean False.
    '''
    pass



def main():
    """
    This function takes in no arguments. It calls all of the
    other functions to make the program work as well as assign
    some of the necessary primary variables like player data
    and the pokemon csv. If player's pokemon data is empty, adds
    one pokemon to their list of pokemon via the catch_pokemon function.
    """
    pass


def run_safari(player_data):
    """
    Takes in player data as a parameter, then runs the pokemon safari in a new window, rendering the
    graphics when necessary. Calls the three weirdos minigame to determine catch success and proctors the
    results, calling catch_pokemon (allowing player to catch a random pokemon) if said player is successful
    """
    pass


def three_weirdos():
    """
     Takes in no parameters and runs the minigame that will be used to catch pokemon. Chooses a random 
    game out of the 6 from the dictionary above by using "seed", and selects names from a list of
    popular anime/video games (Steins;Gate, Death Note, Cyberpunk: Edgerunners, etc.) as the
    people in these puzzles. This is a variation on a popular logic puzzle that involves determining
    who must be lying/telling the truth, and can be solved by using tables or other forms of logic.
    These specific examples were taken from the Three Weirdos dungeon puzzle in Hypixel Skyblock.
    """
