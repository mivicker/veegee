import numpy as np
from bs4 import BeautifulSoup

command_lens = {
    "m":1,
    "M":1,
    "c":3,
    "C":3,
    "l":1,
    "L":1,
    "h":1,
    "H":1,
    "z":0,
    "Z":0,
    "a":7,
    "A":7,
    "q":2,
    "Q":2
}

def split_commands_points(path_tag):
    dstring = path_tag["d"]
    dstring_list = dstring.split()

    commands = []
    counter = 0
    for item in dstring_list:
        if counter == 0:
            if item.isalpha():
                current_command = item
                continue
            commands.append(current_command)
            counter = command_lens[current_command]
        counter -= 1
    points = [point for point in dstring_list if not point.isalpha()]
    return commands, points

def points_to_numpy(dpoints):
    points_array = np.zeros((len(dpoints),2))
    for row, point in enumerate(dpoints):
        vals = point.split(",")
        points_array[row] = [float(vals[0]), float(vals[1])]
    return points_array

def commands_to_indicies(commands):
    command_counts = {command:0 for command in command_lens.keys()}
    command_indicies = {}
    index = 0
    current_command = 'Null'
    for command in commands:
        if command != current_command:
            current_command = command
            command_len = command_lens[command]
        command_end = index + command_len
        command_indicies[command + str(command_counts[command])] = (index, command_end)
        command_counts[command] += 1
        index = command_end
    return command_indicies

element_classes = {
    'path': Path
}

def make_shape_object(shape_tag):
    objectClass = element_classes[shape_tag.name]
    return objectClass(shape_tag)
