class Sudoku_board:
    matrix = [[[]]]

    def __inin__(self):
        ## Empty 9x9x9 list: https://stackoverflow.com/questions/10668341/create-3d-array-using-python
        [[[0 for _ in range(9)] for _ in range(9)] for _ in range(9)]
        for x in range(9):
            for y in range(9):
                for z in range(9):
                    self.matrix[x][y][z] = z


