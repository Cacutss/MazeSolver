from cell import *
from window import *
import time

class Maze:
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win = Window(1920,1080)):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                row.append(Cell(Point(0,0),Point(0,0),self._win))
            self._cells.append(row)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
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
        self._cells[0][0].has_
