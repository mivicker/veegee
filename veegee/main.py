# MVP
import numpy as np
from bs4 import BeautifulSoup

class Path:
    def __init__(self, path_tag):
        self.commands, points = split_commands_points(path_tag)
        self.points_array = points_to_numpy(points)
        self.command_indicies = commands_to_indicies(self.commands)

class Group:
    def __init__(self, layer_tag):
        self.name = layer_tag["id"]
        self.elements = [make_shape_object(item)
                         for item in layer_tag
                         if item != '\n']

class SvgRoot:
    def __init__(self, svg_string):
        self.soup = BeautifulSoup(svg_string, "html.parser")
        self.layers = [Group(layer) for layer in self.soup.find_all("g")]
