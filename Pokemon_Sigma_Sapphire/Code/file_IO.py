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
    Words
    """
    with open(file_path, "r") as file:
        dictionary = json.loads(file)
        return dictionary


def push_json(file_path, dictionary, mode):
    """
    Words
    """
    with open(file_path, mode="w") as file:
        try:
            json.dump(dictionary, file, mode)
        except:
            return False









