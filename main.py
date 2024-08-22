from window import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 10, 50, 50, win)
    maze.solve()
    win.wait_for_close()

main()