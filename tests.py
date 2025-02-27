import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12 
        num_rows = 10
        m1 = Maze(50,50,num_rows,num_cols,50,50,1)
        self.assertEqual(
                len(m1._cells),
                num_rows,
        )
        self.assertEqual(
                len(m1._cells[0]),
                num_cols,
        )

    def test_maze_check_paths(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(50,50,num_rows,num_cols,50,50)

        for i in range(m1._num_rows-1):
            for j in range(m1._num_cols-1):
                possible_path = []
                m1._search_cells(i,j,possible_path)
                for path in possible_path:
                    print(m1._check_possible_path((i,j),path))

if __name__ == "__main__":
    unittest.main()
