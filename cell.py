from window import Window
from point import Point
from line import Line

class Cell():
    def __init__(self, window: Window = None, x_1 = 0, x_2 = 0, y_1 = 0, y_2 = 0, has_left = True, has_right = True, has_top = True, has_bottom = True):
        self.has_left_wall = has_left
        self.has_right_wall = has_right
        self.has_top_wall = has_top
        self.has_bottom_wall = has_bottom
        self.__x1 = x_1
        self.__x2 = x_2
        self.__y1 = y_1
        self.__y2 = y_2
        self.visited = False
        self.__win = window

    def draw(self, x1, x2, y1, y2):
        # set corner coordinates
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        # draw each wall, if it doesn't have a wall draw it with the same color code of the background
        # (bg colour based on OS, may not be the same colour for others)
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "#d9d9d9")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
        else:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "#d9d9d9")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "#d9d9d9")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")
        else:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        # set colour to trace maze, if undo is true, grey out the line to represent dead end
        fill_colour = ""
        if undo:
            fill_colour = "gray"
        else:
            fill_colour = "red"
        # find the centers of the cells the line is being drawn between
        x1 = (self.__x1 + self.__x2) / 2
        y1 = (self.__y1 + self.__y2) / 2
        x2 = (to_cell.__x1 + to_cell.__x2) / 2
        y2 = (to_cell.__y1 + to_cell.__y2) / 2
        self.__win.draw_line(Line(Point(x1, y1), Point(x2, y2)), fill_colour)