from cell import Cell
from window import Window
import time
import random

class Maze():
    def __init__(self, x1, y1, rows, cols, cell_size_x, cell_size_y, win: Window = None, seed = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__rows = rows
        self.__cols = cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.cells = [[None for x in range(rows)] for y in range(cols)]
        # If passed a seed, use it to generate random maze
        if seed:
            seed = random.seed(seed)
        
        # create maze
        self.__create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0, 0)
        self.reset_cells_visited()
    
    def __create_cells(self):
        # populate 2D list with cell objects
        for i in range(self.__cols):
            for j in range(self.__rows):
                self.cells[i][j] = Cell(self.__win)
        # draw each cell
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        # calculate corners of inidvidual cells
        cell_x1 = self.__x1 + (self.__cell_size_x * i)
        cell_x2 = cell_x1 + self.__cell_size_x
        cell_y1 = self.__y1 + (self.__cell_size_y * j)
        cell_y2 = cell_y1 + self.__cell_size_y
        # draw cell
        self.cells[i][j].draw(cell_x1, cell_x2, cell_y1, cell_y2)
        self.__animate()

    def break_entrance_and_exit(self):
        # break entrance wall
        self.cells[0][0].has_top_wall = False
        # break exit wall
        self.cells[self.__cols - 1][self.__rows - 1].has_bottom_wall = False
        # draw entrance and exits
        self.__draw_cell(0, 0)
        self.__draw_cell(self.__cols - 1, self.__rows - 1)

    def __animate(self):
        # redraw window and allow delay to see eah frame
        self.__win.redraw()
        time.sleep(0.05)

    def break_walls_r(self, i, j):
        # mark current cell as visited
        self.cells[i][j].visited = True
        while True:
            # create empty list to hold next cells to visit y their indices
            to_visit = []
            if i > 0 and self.cells[i-1][j].visited == False:
                    to_visit.append((i-1, j))
            if i != self.__cols - 1 and self.cells[i+1][j].visited == False:
                    to_visit.append((i+1, j))
            if j > 0 and self.cells[i][j-1].visited == False:
                    to_visit.append((i, j-1))
            if j < self.__rows - 1 and  self.cells[i][j+1].visited == False:
                    to_visit.append((i, j+1))
            # if there is no where else to go, draw cell with broken wall and return
            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return
            # if there are other cells to go to, randomly select one and recursively call function with next indices
            else:
                rand_dir = random.randrange(0, len(to_visit))
                next_index = to_visit[rand_dir]
                #LEFT
                if next_index[0] == i-1:
                    self.cells[i][j].has_left_wall = False
                    self.cells[i-1][j].has_right_wall = False
                #RIGHT
                if next_index[0] == i+1:
                    self.cells[i][j].has_right_wall = False
                    self.cells[i+1][j].has_left_wall = False
                #UP
                if next_index[1] == j-1:
                    self.cells[i][j].has_top_wall = False
                    self.cells[i][j-1].has_bottom_wall = False
                #DOWN
                if next_index[1] == j+1:
                    self.cells[i][j].has_bottom_wall = False
                    self.cells[i][j+1].has_top_wall = False
                
                self.break_walls_r(next_index[0], next_index[1])
    
    def reset_cells_visited(self):
        #reset 'visited' on all cells for solving algorithm
        for i in range(self.__cols):
            for j in range(self.__rows):
                 self.cells[i][j].visited = False

    def solve_r(self, i, j):
        #redraw window and mark current cell as visited
        self.__animate()
        self.cells[i][j].visited = True

        #return true if at the goal
        if i == self.__cols - 1 and j == self.__rows - 1:
            return True
         
        #Check each direction and if there is a wall
        #LEFT
        if i > 0 and not self.cells[i][j].has_left_wall and not self.cells[i-1][j].visited:
            self.cells[i][j].draw_move(self.cells[i-1][j])
            if self.solve_r(i-1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i-1][j], True)
        #RIGHT
        if i < self.__cols and not self.cells[i][j].has_right_wall and not self.cells[i+1][j].visited:
            self.cells[i][j].draw_move(self.cells[i+1][j])
            if self.solve_r(i+1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i+1][j], True)
        #UP
        if j > 0 and not self.cells[i][j].has_top_wall and not self.cells[i][j-1].visited:
            self.cells[i][j].draw_move(self.cells[i][j-1])
            if self.solve_r(i, j-1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j-1], True)
        #DOWN
        if j < self.__rows and not self.cells[i][j].has_bottom_wall and not self.cells[i][j+1].visited:
            self.cells[i][j].draw_move(self.cells[i][j+1])
            if self.solve_r(i, j+1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j+1], True)
        return False
        

    def solve(self):
        # make the first call of recursive solve function
        return self.solve_r(0, 0)