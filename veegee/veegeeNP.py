import numpy as np
import codecs
import re
from bs4 import BeautifulSoup

"""---------------------- from SVG to numpy-based object"""
def list_paths(svg_string):
    soup = BeautifulSoup(svg_string, "html.parser")
    return [str(path).strip() for path in soup.find_all("path")]

def extract_dstring(path_string):
    pattern = r' d="([^"]*)' #returns " d=" until the closing quotes
    return re.findall(pattern, path_string)[0]

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

command_counts = {command:0 for command in command_lens.keys()}

def split_commands_points(path_string):
    dstring = extract_dstring(path_string)
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
    global command_counts
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

"""---------------------- classes to build up SVG"""
class DPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return DPoint(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'{self.x} {self.y}'

class MoveTo:
    def __init__(self, end_point):
        self.point = str(end_point)

    def __str__(self):
        return f'M {self.point}'

class LineTo:
    def __init__(self, end_point):
        self.point = str(end_point)

    def __str__(self):
        return f'L {self.point}'

class CurveTo:
    def __init__(self, arm_one, arm_two, end_point):
       self.arm_one = str(arm_one)
       self.arm_two = str(arm_two)
       self.end_point = str(end_point)

    def __str__(self):
        return f'C {self.arm_one}, {self.arm_two}, {self.end_point}'

class QTo:
    def __init__(self, arm, end_point):
        self.arm = str(arm)
        self.end_point = str(end_point)

    def __str__(self):
        return f'Q {self.arm}, {self.end_point}'

class DCommands: #This might be useful later on as I build with numpy
    pass

class Styling: #There might be some reason to build this as an object IDK :/.
    pass

class Path:
    def __init__(self, d_commands, styling):
        self.d_commands = [str(command) for command in d_commands]
        self.styling = styling #This is a dictionary of the styling.

    def __add__(self, other):
        pass

    def __str__(self):
        command_str = ' '.join(self.d_commands)
        return f'<path d="{command_str}" {self.styling}/>'

    def __len__(self):
        #This will return the lenth of the path based on # of elements.
        pass
"""
with open("Templates/svgmain.txt", "r", encoding='utf-8') as f:
     svg_body_template = f.read()

class SVG_file: #Rename this
    global svg_body_template
    def __init__(self, elements_list):
        self.template = svg_body_template
        self.elements_list = [str(element) for element in elements_list]

    def __str__(self):
        shapes = self.elements_list
        shapes = '\n\t'.join(shapes)
        decoded = codecs.escape_decode(bytes(('\n\t' + shapes), "utf-8"))[0].decode("utf-8")
        svg_body = svg_body_template.format(width = "500", height="300", body=decoded)
        return svg_body
"""


"""---------------------- major veegee classes"""
class veegeePath:
    def __init__(self, path_string):
        self.commands, points = split_commands_points(path_string)
        self.points_array = points_to_numpy(points)
        self.command_indicies = commands_to_indicies(self.commands)

class veegee:
    def __init__(self, svg_file):
        pass
