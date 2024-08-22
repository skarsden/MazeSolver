from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(height=height, width=width)
        self.__canvas.pack()
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        # update window to show changes
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_colour):
        #draw a line in window
        line.draw(self.__canvas, fill_colour)

    def wait_for_close(self):
        # infinite loop that updates window until it is closed
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        # breaks loop in wait_for_close()
        self.__is_running = False