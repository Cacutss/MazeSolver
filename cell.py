from point import *

class Cell:
    def __init__(self,p1,p2,win):
        self.has_right_wall = True
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = p1.x
        self._x2 = p2.x
        self._y1 = p1.y
        self._y2 = p2.y
        self._win = win
    
    def draw(self,color = "black"):
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)),color)
        else:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)),"#d9d9d9")
        if self.has_bottom_wall: 
            self._win.draw_line(Line(Point(self._x2,self._y2),Point(self._x1,self._y2)),color)
        else:
            self._win.draw_line(Line(Point(self._x2,self._y2),Point(self._x1,self._y2)),"#d9d9d9")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)),color)
        else:
            self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)),"#d9d9d9")
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)),color) 
        else:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)),"#d9d9d9")

    def draw_move(self, to_cell, undo = False):
        color = "grey"
        if undo:
            color = "red"
        self._win.draw_line(Line(Point((self._x2 + self._x1) // 2, (self._y2 + self._y1) //2),Point((to_cell._x2 + to_cell._x1) // 2, (to_cell._y2 + to_cell._y1) //2)),color)
