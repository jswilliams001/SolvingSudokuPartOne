import time
import unittest
from sudoku_solver0 import solve_sudoku, is_valid_sudoku, print_sudokus


def test_time(method):
    def timed(*args, **kw):
        tstart = time.time()
        result = method(*args, **kw)
        tend = time.time()
        print(f"{method.__name__}: {tend - tstart} seconds")
        return result
    return timed


# noinspection DuplicatedCode
class SudokuSolverTestLarge(unittest.TestCase):

    def setUp(self):
        self.test_invalid0 = [[ 0,  0,  3,  1,    0,  9,  7,  0,    0,  0, 13,  2,    8,  0,  0,  0],
                              [ 0,  7,  0, 14,    4,  0,  0, 15,    0,  0,  0,  0,    5,  3,  0,  0],
                              [ 4,  0,  9,  0,    1, 10, 11,  0,    0,  0,  0,  7,    0, 13, 15, 16],
                              [11, 13,  0,  2,    0, 14,  0,  0,    0,  0,  4,  0,   10,  1,  0,  0],

                              [ 0, 12,  7,  0,    8,  0,  0,  0,    0,  0,  0,  7,    0, 10,  4,  0],
                              [16,  0,  2, 15,    0,  5,  1,  6,    0, 11,  0,  4,    0,  0,  0, 13],
                              [ 1,  0, 14,  0,    0,  2,  0,  0,    9,  6,  0,  0,    0, 11, 16,  0],
                              [ 0,  6,  0,  0,    0, 13,  0,  0,    7,  0,  0,  0,    0, 15,  0,  5],

                              [ 0,  0,  0,  0,    0,  0,  2,  9,    0,  0,  0,  0,    0, 12, 11,  8],
                              [ 0,  0,  0,  0,    0,  8, 14,  0,    0, 15,  9,  0,    0,  0, 10,  0],
                              [ 9,  0,  0, 16,    0,  0,  0,  0,    0,  8,  1,  6,    0,  5, 13,  0],
                              [ 7,  0,  8,  0,    0,  6,  0,  0,    0,  0, 10,  0,   14,  9,  0,  4],

                              [13, 15,  0,  5,    0,  0,  0,  0,    0,  0,  0, 16,    3,  0,  0, 14],
                              [ 0,  2, 16,  7,   14,  0,  5, 11,    1,  0, 15, 13,    0,  0, 12,  0],
                              [ 0,  0, 11,  0,   15,  0,  6,  0,    3,  2,  7,  0,    0, 16,  0,  9],
                              [0,   0, 10,  0,    0,  4,  0, 13,   12,  0,  0,  5,   11,  0,  7,  0]]

        self.test_valid__0 = [[ 9,  0,  0,  0,   13,  0,  0,  0,    0,  0,  0, 14,   16,  0,  0,  0],
                              [16,  0,  0, 14,    7,  9,  0,  8,    0,  3,  6, 10,    0,  0, 15,  0],
                              [ 0,  2,  0, 15,   10,  4,  0,  0,    0,  0, 13, 16,    8, 14, 11, 12],
                              [ 0, 10,  0,  3,    0,  0,  0,  6,    0,  0,  0, 11,    0,  0,  0,  1],

                              [ 0,  9,  5,  6,    0,  0, 16,  0,    0,  0,  1,  0,    0, 11,  0,  0],
                              [ 3,  0,  1, 16,    0,  0,  7, 12,    0,  0,  4, 15,    0,  0,  9,  0],
                              [ 0,  4,  0,  0,    1,  0, 13,  0,    0,  0,  0,  0,   15,  7,  0,  8],
                              [ 0,  0,  0,  0,    0,  2,  0,  9,    0,  0, 16,  0,    0,  5,  0,  4],

                              [ 0,  0,  6,  7,   12, 14,  0,  4,    0,  9, 10,  5,    0, 15,  2,  0],
                              [ 0, 16, 14,  0,    9,  1,  0,  7,    0,  0, 15,  6,    0,  0,  0,  5],
                              [ 0,  1,  0, 11,    8,  0,  0,  3,   16,  0, 14,  0,    0,  0,  0,  0],
                              [ 0,  5, 13,  0,    0,  0,  6, 15,    4,  8,  0,  0,    0,  1,  7,  3],

                              [13,  6,  0,  5,    0,  7,  9,  0,    0,  0, 12,  3,   10,  8,  0, 15],
                              [ 0,  0,  2,  0,   15,  0,  0, 11,    0, 16,  0,  4,    0,  3, 14,  0],
                              [12, 14,  0,  8,    5, 10,  4,  0,    0,  0,  0,  0,    6,  2,  0,  0],
                              [ 0, 15,  0,  4,    0,  0,  0, 13,    0,  0,  0,  1,    0,  0,  5,  7]]

    #@test_time
    def test_solve_sudoku_large(self):
        result = solve_sudoku(self.test_valid__0, True)
        print()
        print_sudokus(result)
        self.assertTrue(all(result))

    @test_time
    def test_is_valid_sudoku(self):
        result = is_valid_sudoku(self.test_invalid0)
        self.assertEqual(result[0], False)


if __name__ == '__main__':
    unittest.main()