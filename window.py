from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.height = height
        self.width = width
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.canvas = Canvas(height = self.height,width=self.width)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW",self.close)
    
    def draw_line(self,line,fill_color):
        line.draw(self.canvas,fill_color)
    
    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        
    def close(self):
        self.running = False
