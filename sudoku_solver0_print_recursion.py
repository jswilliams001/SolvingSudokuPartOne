from math import sqrt
from collections import Counter
from pprint import pprint
"""
This version of solve_sudoku() prints every step in the backtracking recursive algorith. There are no options
to turn of the printing.
"""

debug = False


def is_valid_sudoku(matrix: list[list[int]]) -> tuple[bool, int, int, list[int]]:
    """
    :param matrix: an n x n Sudoku grid represented as a list of lists. Each inner list represents a row of the grid and
    contains integers from 0 to the length of each row and colum. 0 represents an empty cell.
    :return: a tuple containing the validity of the Sudoku grid, the length of the grid, the size of each
    sub-region, and the boundaries of the sub-regions in the grid.
    """
    length, region_size, boundaries = get_region_size_and_boundaries(matrix)
    region_map = {n: n//region_size for n in range(length)}

    cell_vals = Counter(
        key
        for row_index, row_vals in enumerate(matrix)
        for col_index, cell_val in enumerate(row_vals)
        if cell_val != 0 for key in (
            (row_index, cell_val), (str(col_index), str(cell_val)),
            (region_map[row_index], region_map[col_index], cell_val)  # dict lookups are far more efficient that math
            # (row_index // region_size, col_index // region_size, cell_val)
        )
    )  # key generates a list of tuples that should be unique if there are no duplicates in row, col, or sub-area

    if debug:
        print(f"{region_size=} {length=} {boundaries=}")
        print(cell_vals)
    valid = max(cell_vals.values(), default=0) <= 1  # default is there for the case of an empty set (all zeros)
    return valid, length, region_size, boundaries


def solve_sudoku(matrix: list[list[int]], all_results=False) -> list[list[list[int]]]:
    """
    :param matrix: An n x n matrix representing the Sudoku puzzle. Each element in the matrix is an integer from 0
    to the length of each row and column. 0 represents an empty cell.
    :param all_results: A boolean value indicating whether to return all possible solutions (True) or just the first
    solution (False). Default value is False.
    :return: A list of solutions to the Sudoku puzzle. Each solution is represented as an n x n matrix, matching the
    size of the input matrix.
    """
    valid, length, region_size, boundaries = is_valid_sudoku(matrix)
    region_map = gen_region_map(length, region_size)

    if debug:
        print(f"{length=} {region_size=} {boundaries=} {valid=}")

    def is_valid_to_add(m_matrix, m_length, row, col, val):
        # Check if the number is not repeated in the current row, column and region
        for x in range(m_length):
            r_row, c_col = region_map[row][col][x]
            if m_matrix[row][x] == val or m_matrix[x][col] == val or m_matrix[r_row][c_col] == val:
                return False
        return True

    def solve(inner_matrix, inner_result_list=None):
        print_sudokus(inner_matrix)
        for row in range(length):
            print(f"-outer loop 0 {row=}")
            for col in range(length):
                print(f"--Loop 1 {col=}")
                if inner_matrix[row][col] == 0:
                    for val in range(1, length+1):
                        print(f"--Loop 2, val in range() trying {row=} {col=} {val=}")
                        if is_valid_to_add(inner_matrix, length, row, col, val):
                            inner_matrix[row][col] = val  # try a value
                            print(f"--Adding {row=} {col=} {val=}")
                            print("--Calling solve()")
                            if solve(inner_matrix, inner_result_list):  # recursion
                                if all_results:
                                    print(f"--solve() returned True. Append to results list")
                                    print_sudokus(inner_matrix)
                                    inner_result_list.append([row[:] for row in inner_matrix])
                                else:
                                    print(f"--solve() returned True. Return True from outer Solve()")
                                    return True
                            inner_matrix[row][col] = 0  # value failed, reset cell to 0
                            if all_results:
                                print(f"Reset {row=} {col=} to 0 and backtrack to solve another solution or end.")
                            else:
                                print(f"--solved() returned False. Reset {row=} {col=} to 0")
                    print("--Loop 2 val in range() ended. Return False")
                    return False
        print("Outer loop 0 ended. Return True.")
        return True
    if valid:
        results_list = []
        if all_results:
            solve(matrix, results_list)
        else:
            solve(matrix)
            results_list.append([row[:] for row in matrix])
        return results_list
    else:
        print("Not a valid sudoku matrix. Aborting Mission.")
    return matrix


# unused function
def is_valid_to_add__(region_size, matrix, length, row, col, val):
    # This is here so that you can easily see for yourself the performance gain when substituting memory
    # operations for math operations.
    # replace line 64 with: if is_valid_to_add__(region_size, inner_matrix, length, row, col, val):
    for x in range(length):
        if matrix[row][x] == val or matrix[x][col] == val or \
           matrix[region_size * (row // region_size) + x // region_size] \
                [region_size * (col // region_size) + x % region_size] == val:
            return False
    return True


def gen_region_map(length, region_size):
    z = {}
    for row in range(length):
        z.update({row: {}})
        for col in range(length):
            z[row].update({col: {}})
            for x in range(length):
                z[row][col].update({x: ((row // region_size) * region_size + x // region_size, \
                                         (col // region_size) * region_size + x % region_size)})
    if debug:
        pprint(z)
    return z


def get_region_size_and_boundaries(matrix: list[list[int]]) -> tuple[int, int, list[int]]:
    if (length := len(matrix)) == (width := len(matrix[0])) and (float(region_l := sqrt(length))).is_integer() \
            and all(len(row) == length for row in matrix):
        r_size = region_l.__floor__()
        # matrix is square so only calculate row
        boundaries = [y for y in range(0, length, r_size)]
        return length, r_size, boundaries
    else:
        raise ValueError(f"sudoku matrix not of a valid size {length=} {width=}")


def depth(list_of_lists):
    j = 0
    for item in list_of_lists:
        if isinstance(item, list):
            j = max(depth(item), j)
    return j + 1


def print_sudokus(matrix: list[list[list[int]]]):
    def print_s(matrix: list[list[int]]):
        # Assuming a valid sudoku matrix without safety checking
        row_len = len(matrix)
        region = int(sqrt(row_len))
        digit_width = len(str(row_len))
        padding = 2 + digit_width
        separator = f"-" * (padding * row_len + region + 1)
        for c in range(row_len):
            if 0 == c % region:
                print(separator)
            string = ""
            for r in range(row_len):
                if 0 == r % region:
                    string += "|"
                string += f"{str(matrix[c][r]):^{padding}}"
            string += "|"
            print(string.replace(" 0", " ."))
        print(separator)
    if 2 == depth(matrix):  # In case in_valid_sudoku() returns Fail
        print_s(matrix)
    else:
        for x in matrix:
            print_s(x)


if __name__ == '__main__':
    t1 = [[1, 0,  0, 0],
          [0, 0,  0, 0],

          [3, 0,  0, 0],
          [0, 0,  0, 0]]

    test = solve_sudoku(t1, False)
    print_sudokus(test)
    print()
    print()
    test = solve_sudoku(t1, True)
    print_sudokus(test)


