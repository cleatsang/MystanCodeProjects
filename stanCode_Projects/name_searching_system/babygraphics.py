"""
File: babygraphics.py
Name: Audrey Tsang
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

#  Constants
FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = int(((width - GRAPH_MARGIN_SIZE*2) / len(YEARS) * year_index) + GRAPH_MARGIN_SIZE)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT,
                           width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE+TEXT_DX,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    n = -1  # Check the order of the color.
    unit = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000  # The unit for per row.
    # Create a list to store the x-coordinates of each year.
    year_x = []
    for i in range(len(YEARS)):
        year_x.append(get_x_coordinate(CANVAS_WIDTH, i))
    # Starts drawing a line chart.
    for name in lookup_names:
        #  Check the order of color for this run.
        if n > 3:
            n == 0
        else:
            n += 1
        #  Creates a list to store the ranking of each year in text version and another list in number version.
        ranking = []
        rank_y = []
        for i in range(len(YEARS)):
            if str(YEARS[i]) in name_data[name]:
                ranking.append(name_data[name][str(YEARS[i])])
                rank_y.append(float(GRAPH_MARGIN_SIZE + int(ranking[i]) * unit))
            else:  # If the name doesn't have ranking in this year.
                ranking.append('*')
                rank_y.append(CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
            #  Add the text for this year.
            canvas.create_text(year_x[i], rank_y[i], text=name+str(ranking[i]), anchor=tkinter.SW, fill=COLORS[n])
            #  Draw the line for this year(when it's not the first year).
            if i != 0:
                canvas.create_line(year_x[i-1], rank_y[i-1], year_x[i], rank_y[i], width=LINE_WIDTH, fill=COLORS[n])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
