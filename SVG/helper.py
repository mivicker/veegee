import codecs

def build_img(shapes_string, file_name="test.svg"):
    """
    This takes a string of svg shape strings and returns a formatted svg file.
    """
    with open("Templates/svgmain.txt", 'r', encoding = "utf-8") as f:
        svg_body_template = f.read()

    decoded_string = codecs.escape_decode(bytes(shapes_string, "utf-8"))[0].decode("utf-8")
    svg_body = svg_body_template.format(width = "300", height = "300", body=decoded_string)
    with open(file_name, "w", encoding = "utf-8") as f:
        f.write(svg_body)

def make_rect(attr_dict):
    """
    Takes a dictionary that maps rect svg keywords to the desired values.
    """
    with open("Templates/rect.txt", "r", encoding = "utf-8") as data:
        rect_template = data.read()

    return rect_template.format_map(attr_dict)


def make_circle(attr_dict):
    """
    Takes a dictionary that maps circle svg keywords to the desired values.
    """
    with open("Templates/circle.txt", "r", encoding = "utf-8") as data:
        circle_template = data.read()

    return circle_template.format_map(attr_dict)


def make_text(attr_dict):
    """
    Takes a dictionary that maps text svg keywords to the desired values.
    """
    with open("Templates/text.txt", "r", encoding = "utf-8") as data:
        text_template = data.read()

        return text_template.format_map(attr_dict)
