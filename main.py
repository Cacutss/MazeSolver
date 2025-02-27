from maze import *

def main():
    maze = Maze(x1 = 100, y1 = 50,num_cols= 15,num_rows= 10,cell_size_x = 50,cell_size_y = 50)
    maze.solve()
    maze._win.wait_for_close()

if __name__ == "__main__":
    main()
