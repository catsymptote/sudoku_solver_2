class Sudoku_solver:
    matrix = [[[]]]

    def __inin__(self, board):
        ## Empty 9x9x9 list: https://stackoverflow.com/questions/10668341/create-3d-array-using-python
        [[[0 for _ in range(9)] for _ in range(9)] for _ in range(9)]
        # Loop
        for x in range(9):
            for y in range(9):
                # Board cell has no value.
                if (board[x][y] == 0):
                    # Fill with 1-9
                    for z in range(9):
                        self.matrix[x][y][z] = z
                # Board cell has a (none zero) value.
                else:
                    self.matrix[x][y][:1]
                    self.matrix[x][y][0] = board[x][y]
                    #del self.matrix[x][y][:]
                    #self.matrix[x][y].append(board[x][y])



