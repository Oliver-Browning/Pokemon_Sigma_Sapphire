def fetch_list(file_path, show_first = True):
    """
    Takes a file path file_path, and a boolean show_first of as arguments.
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







