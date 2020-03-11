#This sets the values that will be used to fill the rect parameters
sizes = np.arange(1,35) * 10
colors = ["#885053", "#fe5f55", "#777da7", "#94c9a9", "#c6ecae"]
sizes = np.flip(sizes)

#This is where the body of the text is created.
rects = ""
for index, size in enumerate(sizes):

    shape_attr = size_dict = {"width": size, "height": size, "fill": colors[index%len(colors)]}
    new_rect = make_rect(shape_attr)

    rects += "\t" + new_rect + "\n"

build_img(rects, file_name = "test2.svg")
