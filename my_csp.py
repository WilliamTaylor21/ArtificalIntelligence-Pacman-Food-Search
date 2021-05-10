from sudoku import Sudoku
from copy import deepcopy
import numpy as np



class CSP_Solver(object):
    """
    This class is used to solve the CSP with backtracking using the minimum value remaining heuristic.
    HINT: you will likely want to implement functions in the backtracking sudo code in figure 6.5 in the text book.
            We have provided some prototypes that might be helpful. You are not required to use any functions defined
            here and can modify any function other than the solve method. We will test your code with the solve method
            and so it must have no parameters and return the type it says. 
         
    """
    def __init__(self, puzzle_file):
        '''
        Initialize the solver instance. The lower the number of the puzzle file the easier it is. 
        It is a good idea to start with the easy puzzles and verify that your solution is correct manually. 
        You should run on the hard puzzles to make sure you aren't violating corner cases that come up.
        Harder puzzles will take longer to solve.
        :param puzzle_file: the puzzle file to solve 
        '''
        self.sudoku = Sudoku(puzzle_file) # this line has to be here to initialize the puzzle
        # print ("Sudoku", Sudoku.board_str(self.sudoku))
        # print("board", self.sudoku.board) - List of Lists 
        self.num_guesses = 0
        # self.unassigned = deque()
        self.assignment = {}
        
        # make domian the Given Puzzle
        self.domains = deepcopy(self.sudoku.board)
        # Overwrite 0's with their possiblilities.
        for row in range(0,9):
            for col in range(0,9):
                # extract value
                value = self.sudoku.board[row][col]
                if value == 0:
                    self.domains[row][col] = [1,2,3,4,5,6,7,8,9]
                    # add this index to unassigned for faster look ups
                    # self.unassigned.append((row,col))
                else: 
                    self.domains[row][col] = value
                    self.assignment[(row, col)] = value

        vars=[]
        # self.csp = CSP(vars, self.domains)

    def find_next_empty_space(self):
        for r in range(9):
            for c in range(9):
                if self.sudoku.board[r][c] == 0:
                    return r,c
        return None, None
            
    def is_guess_valid(self, guess, row, col):
        row_value = self.sudoku.board[row]
        if guess in row_value:
            return False
            
        column_value = [self.sudoku.board[i][col] for i in range(9)]
        if guess in column_value:
            return False
        
        x = (row // 3) * 3
        y = (col // 3) * 3
        for r in range(x, x + 3):
            for c in range(y, y + 3):
                if self.sudoku.board[r][c] == guess:
                    return False
        return True
        
        
    def solve(self):
        self.backtracking_search()
        print ( self.sudoku.board)
        print("number of guesses:",self.num_guesses)
        return self.sudoku.board, self.num_guesses

    def backtracking_search(self):
        row, col = self.find_next_empty_space()
        if row is None:
            return self.sudoku.board, self.num_guesses
        for guess in range(1,10):
            self.num_guesses += 1
            if self.is_guess_valid(guess, row, col):
                self.sudoku.board[row][col] = guess
                if self.backtracking_search():
                    return True
                
            self.sudoku.board[row][col] = 0
        return False



if __name__ == '__main__':
    csp_solver = CSP_Solver('puz-100.txt')
    solution, guesses = csp_solver.solve()

