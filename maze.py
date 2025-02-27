from cell import *
from window import *
import random
import time

class Maze:
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,seed = None,win = Window(1920,1080)):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            self._seed = random.seed(seed)
        else:
            self._seed = 0
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                row.append(Cell(Point(0,0),Point(0,0),self._win))
            self._cells.append(row)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i,j)


    def _draw_cell(self,i,j):
        self._cells[i][j]._x1 = self._x1 + (j * self._cell_size_x)
        self._cells[i][j]._x2 = self._x1 + ((j+1) * self._cell_size_x)
        self._cells[i][j]._y1 = self._y1 + (i * self._cell_size_y)
        self._cells[i][j]._y2 = self._y1 + ((i+1) * self._cell_size_y)
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        max = [len(self._cells)-1,len(self._cells[0])-1]
        self._cells[max[0]][max[1]].has_top_wall = False
        self._cells[max[0]][max[1]].has_left_wall = False
        self._cells[max[0]][max[1]].has_right_wall = False
        self._cells[0][0].has_right_wall = False
        self._cells[0][0].has_bottom_wall = False
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0,0)
        self._draw_cell(max[0],max[1])
    
    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i == len(self._cells) and j == len(self._cells[i]):
                self._draw_cell(i,j)
                return
            else:
                self._search_cells(i,j,to_visit)
                if to_visit == []:
                    self._draw_cell(i,j)
                    return
            direction = random.randint(0,len(to_visit)-1)
            self._break_wall((i,j),to_visit[direction])
            self._break_walls_r(to_visit[direction][0],to_visit[direction][1])

    def _search_cells(self,i,j,lst):
        if i < self._num_rows-1 and not self._cells[i+1][j].visited:    
            lst.append((i+1,j))
        if i > 0 and not self._cells[i-1][j].visited: 
            lst.append((i-1,j))
        if j < self._num_cols-1 and not self._cells[i][j+1].visited: 
            lst.append((i,j+1))
        if j > 0 and not self._cells[i][j-1].visited:
            lst.append((i,j-1)) 

    
    def _break_wall(self,cell1: tuple,cell2: tuple):
        if cell1[0] < cell2[0]:
            self._cells[cell1[0]][cell1[1]].has_bottom_wall = False
            self._cells[cell2[0]][cell2[1]].has_top_wall = False
        elif cell1[0] > cell2[0]:
            self._cells[cell1[0]][cell1[1]].has_top_wall = False
            self._cells[cell2[0]][cell2[1]].has_bottom_wall = False
        elif cell1[1] < cell2[1]:
            self._cells[cell1[0]][cell1[1]].has_right_wall = False
            self._cells[cell2[0]][cell2[1]].has_left_wall = False
        elif cell1[1] > cell2[1]:
            self._cells[cell1[0]][cell1[1]].has_left_wall = False
            self._cells[cell2[0]][cell2[1]].has_right_wall = False
        self._draw_cell(cell1[0],cell1[1])
        self._draw_cell(cell2[0],cell2[1])
        return
    
    def _check_possible_path(self,cell1: tuple, cell2: tuple):
        if self._cells[cell2[0]][cell2[1]].visited:
            return False
        if cell1[0] < cell2[0]:
            return not self._cells[cell1[0]][cell1[1]].has_bottom_wall and not self._cells[cell2[0]][cell2[1]].has_top_wall
        if cell1[1] < cell2[1]:
            return not self._cells[cell1[0]][cell1[1]].has_right_wall and not self._cells[cell2[0]][cell2[1]].has_left_wall
        if cell1[0] > cell2[0]:
            return not self._cells[cell1[0]][cell1[1]].has_top_wall and not self._cells[cell2[0]][cell2[1]].has_bottom_wall
        if cell1[1] > cell2[1]:
            return not self._cells[cell1[0]][cell1[1]].has_left_wall and not self._cells[cell2[0]][cell2[1]].has_right_wall

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
        return

    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_rows-1 and j == self._num_cols-1:
            print(True)
            return True
        directions = []
        self._search_cells(i,j,directions)
        for direction in directions:
            if self._check_possible_path((i,j),direction):
                self._cells[i][j].draw_move(self._cells[direction[0]][direction[1]])
                if self._solve_r(direction[0],direction[1]):
                    print(True)
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[direction[0]][direction[1]],True)
        print(False)
        return False
                
