# Sudoku Solver and Unit Tests
Code from article: https://joe-on-everything.beehiiv.com/p/solving-sudoku-part-one

## sudoku_solver0.py

This script is a simple, recursive, Sudoku solver. 

It uses a backtracking algorithm. The idea behind it is simple: it tries to place numbers on the Sudoku grid by 
following the Sudoku rules. If no numbers can be placed in a certain position, it 'backs up' to a previous position 
and tries a different number. If it finds a complete grid that obeys all Sudoku 
rules, it will present that as a solution.

## sudoku_solver0_print_recursion.py

This is a modified `sudoku_solver0.py` that includes print statements to visualize the recursion process in the 
terminal.

There are no options to disable the print() statements in the solve() function. 

## uniTest_fast.py

This script is a unit test for the Sudoku solver script using small Sudoku grids for rapid testing.

## uniTest_large.py

This script is unit test using a 16 X 16 grid. It only validates the grid as valid and solves it. It may take in 
excess of 1 minute to complete.


