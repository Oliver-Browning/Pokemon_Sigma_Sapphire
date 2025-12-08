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

import json


def fetch_list(file_path, show_first = True):
    """
    Takes a string file path file_path, and a boolean show_first of as arguments.
    Opens file, and reads into a list called line_list.
    If show_first is False, the first line (header) will 
    not be read into the list. Returns list.
    """
    with open(file_path, "r") as reading:
        lines = reading.readlines()
        line_list = []

        for line in lines:
            line_list.append(line.strip())

        if show_first == False:
            line_list = line_list[1:]

    return line_list


def push_list(file_path, line_list, mode="w"):
    """
    Takes a string file path file_path, a list of data called line_list
    and a string mode for the open mode. Opens/creates file and writes
    the data to the file in the mode specified. For debugging, returns
    boolean False if there was an error.
    """
    with open(file_path, mode) as writing:
        try:
            for line in line_list:
                writing.write(line, "\n")
        except:
            return False


def fetch_json(file_path):
    """
    Takes a string file path file_path as an argument.
    Opens file and converts json data to a dictionary. Returns dictionary.
    """
    with open(file_path, "r") as file:
        dictionary = json.load(file)
        return dictionary


def push_json(file_path, dictionary, mode):
    """
    Takes a string file path file_path, a dictionary called dictionary,
    and a string mode for the open mode. Opens/creates file and writes
    the dictionary to the file in json format in the mode specified. For debugging,
    prints relevant information if there was an error.
    """
    with open(file_path, mode="w") as file:
        try:
            json.dump(dictionary, file, indent = 4) #For possible future reference, the error being caused was due to passing in a mode argument that wasnt meant to be there
        except:
            print("SOMETHING BROKE")
            print(f"This is the filepath: {file_path}")
            print(f"This is the mode: {mode}")
            print(f"This is the all_player_data that was passed in to the function: {dictionary}")
            print(f"This is the datatype of all_player_data: {type(dictionary)}")
            #return False