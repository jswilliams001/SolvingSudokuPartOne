import time
import unittest
from sudoku_solver0 import solve_sudoku, is_valid_sudoku, print_sudokus


# noinspection DuplicatedCode
def test_time(method):
    def timed(*args, **kw):
        tstart = time.time()
        result = method(*args, **kw)
        tend = time.time()
        print(f"{method.__name__}: {tend - tstart} seconds")
        return result
    return timed


# noinspection DuplicatedCode
class SudokuSolverTestCase(unittest.TestCase):

    def setUp(self):
        self.test_empty__0 = [[0] * 4 for _ in range(4)]

        self.test_empty__1 = [[0] * 9 for _ in range(9)]

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

        self.test_sudoku_0 = [[1, 0,  0, 0],
                              [0, 0,  0, 0],

                              [3, 0,  0, 0],
                              [0, 0,  0, 0]]

        self.test_sudoku_1 = [[1, 4,  2, 3],
                              [2, 3,  4, 1],

                              [3, 2,  1, 4],
                              [4, 1,  3, 2]]

        self.test_sudoku_2 = [[0, 9, 0,  0, 0, 3,  0, 1, 0],
                              [0, 2, 0,  0, 5, 0,  9, 4, 0],
                              [0, 0, 0,  4, 0, 0,  0, 0, 7],

                              [0, 0, 2,  1, 4, 0,  8, 5, 0],
                              [0, 1, 0,  0, 9, 0,  0, 0, 0],
                              [4, 0, 0,  0, 0, 6,  1, 0, 0],

                              [8, 0, 0,  0, 0, 2,  7, 0, 0],
                              [0, 0, 0,  0, 0, 0,  4, 2, 3],
                              [0, 0, 0,  0, 0, 0,  0, 6, 0]]

        self.test_sudoku_3 = [[2, 9, 5,  7, 4, 3,  8, 6, 1],
                              [4, 3, 1,  8, 6, 5,  9, 0, 0],
                              [8, 7, 6,  1, 9, 2,  5, 4, 3],

                              [3, 8, 7,  4, 5, 9,  2, 1, 6],
                              [6, 1, 2,  3, 8, 7,  4, 9, 5],
                              [5, 4, 9,  2, 1, 6,  7, 3, 8],

                              [7, 6, 3,  5, 2, 4,  1, 8, 9],
                              [9, 2, 8,  6, 7, 1,  3, 5, 4],
                              [1, 5, 4,  9, 3, 8,  6, 0, 0]]

        self.test_sudoku_4 = [[0, 0, 0,  0, 0, 0,  0, 0, 0],
                              [0, 0, 7,  8, 3, 0,  9, 0, 0],
                              [0, 0, 5,  0, 0, 2,  6, 4, 0],

                              [0, 0, 2,  6, 0, 0,  0, 7, 0],
                              [0, 4, 0,  0, 0, 0,  0, 8, 0],
                              [0, 6, 0,  0, 0, 3,  2, 0, 0],

                              [0, 2, 8,  4, 0, 0,  5, 0, 0],
                              [0, 0, 0,  0, 9, 6,  1, 0, 0],
                              [0, 0, 0,  0, 0, 0,  0, 0, 0]]

        self.test_invalid5 = [[1, 4,  2, 3],
                              [2, 3,  4, 1],

                              [3, 2,  1, 3],
                              [4, 1,  3, 2]]

    @test_time
    def test_solve_sudoku_empty0(self):
        result = solve_sudoku(self.test_empty__0)
        print("4x4 filled, 1 solution")
        print_sudokus(result)
        self.assertTrue(all(result))

    @test_time
    def test_solve_sudoku_empty1(self):
        result = solve_sudoku(self.test_empty__1)
        print("9x9 filled, 1 solution")
        print_sudokus(result)
        self.assertTrue(all(result))

    @test_time
    def test_solve_sudoku_multi2(self):
        result = solve_sudoku(self.test_sudoku_2, True)
        print("16x16 1 solution")
        print_sudokus(result)
        self.assertTrue(all(result))

    @test_time
    def test_solve_sudoku_multi3(self):
        result = solve_sudoku(self.test_sudoku_3, True)
        print("16x16 2 solutions")
        print_sudokus(result)
        self.assertTrue(all(result))

    @test_time
    def test_solve_sudoku_single4(self):
        result = solve_sudoku(self.test_sudoku_4)
        print("16x16 1 solution")
        print_sudokus(result)
        self.assertTrue(all(result))

    @test_time
    def test_solve_sudoku_single5(self):
        result = solve_sudoku(self.test_invalid5)
        print("4x4 1 solution")
        print_sudokus(result)
        self.assertTrue(result)

    @test_time
    def test_is_valid_sudoku_empty0(self):
        result = is_valid_sudoku(self.test_empty__0)
        self.assertEqual(result[0], True)

    @test_time
    def test_is_valid_sudoku_empty1(self):
        result = is_valid_sudoku(self.test_empty__1)
        self.assertEqual(result[0], True)

    @test_time
    def test_is_valid_sudoku_invalid0(self):
        result = is_valid_sudoku(self.test_invalid0)
        self.assertEqual(result[0], False)

    @test_time
    def test_is_valid_sudoku_valid2(self):
        result = is_valid_sudoku(self.test_sudoku_2)
        self.assertEqual(result[0], True)

    @test_time
    def test_is_valid_sudoku_valid3(self):
        result = is_valid_sudoku(self.test_sudoku_3)
        self.assertEqual(result[0], True)

    @test_time
    def test_is_valid_sudoku_valid4(self):
        result = is_valid_sudoku(self.test_sudoku_4)
        self.assertEqual(result[0], True)

    @test_time
    def test_is_valid_sudoku_invalid5(self):
        result = is_valid_sudoku(self.test_invalid5)
        self.assertEqual(result[0], False)


if __name__ == '__main__':
    unittest.main()
