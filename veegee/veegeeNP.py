import numpy as np
import re
from bs4 import BeautifulSoup

"""---------------------- from SVG to numpy-based object"""
def list_elements(svg_string):
    soup = BeautifulSoup(svg_string, "html.parser")
    return [str(path).strip() for path in soup.find_all("path")]

def extract_dstring(path_string):
    pattern = r' d="([^"]*)' #returns " d=" until the closing quotes
    return re.findall(pattern, path_string)[0]

def split_commands_points(path_string):
    dstring = extract_dstring(path_string)
    dstring_list = dstring.split()
    commands = [command for command in dstring_list if command.isalpha()]
    points = [point for point in dstring_list if not point.isalpha()]
    return commands, points

def points_to_numpy(dpoints):
    points_array = np.zeros((len(dpoints),2))
    for row, point in enumerate(dpoints):
        vals = point.split(",")
        points_array[row] = [float(vals[0]), float(vals[1])]
    return points_array
