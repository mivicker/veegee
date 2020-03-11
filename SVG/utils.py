import numpy as np
import codecs
from helper import *

#I need a clear approach to filling the line commands for generative drawing.
#A tree would maybe work best, where the higher nodes are 

class path:
    def __init__(self, d_commands, styling):
        self.d_commands = d_commands
        self.styling = styling

    def __str__(self):
        return f'<path d="{self.d_commands}" {self.styling}/>'
"""
class d_point:
    pass

class move_to(d_point):
    pass

class line_to(d_point):
    pass

class curve_to(d_point):


d_template = "M {x1} {y1} {}"

path_template = '<path d="{d}" {attributes}/>'

build_img()
"""
