import codecs

#In the way the svg reads, you are working from a starting point and each command
#moves you to another point according to some parameters

#Must store each path with all the subobjects and not cast everything to str.

#Need a way to build path out of sub paths meaninfully.
#Maybe keeping the curves relative to one another.


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
        #I really would like to have this.
        #STUDY MORE
        pass

    def __str__(self):
        command_str = ' '.join(self.d_commands)
        return f'<path d="{command_str}" {self.styling}/>'

    def __len__(self):
        #This will return the lenth of the path based on # of elements.
        pass


##I'm not sure how to do this. I want to pull the svg template out of this
##text file and then use it in every instance, but I want it to come along
##Currently going to use a global variable.

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


#This is what the final output should look like for each section.
#We'll figure out the
#<path d="M 10 10 C 20 20, 40 20, 50 10" stroke="black" fill="transparent"/>
#Another example using three points
#<path d="M 10 80 C 40 10, 65 10, 95 80 S 150 150, 180 80" stroke="black" fill="transparent"/>
