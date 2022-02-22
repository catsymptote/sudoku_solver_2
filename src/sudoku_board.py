class Sudoku_board:

    def __init__(self, board=None):
        # Empty 9x9x9 list:
        # https://stackoverflow.com/questions/10668341/create-3d-array-using-python  # noqa

        self.matrix = [[[z + 1 for z in range(9)]
                        for _ in range(9)]
                       for _ in range(9)]

        board = board

        if board is not None:
            for i, row in enumerate(board):
                for j, value in enumerate(row):
                    if value != 0:
                        self.matrix[i][j] = [value]

    def get(self, x=None, y=None, shape=None):
        if shape is None:
            return self.matrix[x][y]
        elif shape == 'row':
            return self.matrix[x]
        elif shape in ['col', 'column']:
            cells = []
            for row_idx, row in enumerate(self.matrix):
                cells.append(row[y])
            return cells
        elif shape in ['sq', 'sqr', 'square', 'cube']:
            x0 = x - x % 3
            x1 = x0 + 3
            y0 = y - y % 3
            y1 = y0 + 3
            # assert False

            cells = []
            for row_idx, row in enumerate(self.matrix):
                for col_idx, cell in enumerate(row):
                    if x0 <= row_idx < x1 and y0 <= col_idx < y1:
                        cells.append(cell)
            return cells

    def set_cell(self, x, y, new_value):
        if type(new_value) is int:
            new_value = [new_value]
        self.matrix[x][y] = new_value

    def check(self):
        for x in range(9):
            for y in range(9):
                block_tags = ['row', 'column', 'square']
                for tag in block_tags:
                    cells = self.get(x, y, shape=tag)
                    cells = [cell[0] for cell in cells if len(cell) == 1]

                    if len(cells) != len(list(set(cells))):
                        return False
        return True

    def finished(self):
        # Check for non-solved or 0's.
        for x in range(9):
            for y in range(9):
                cell = self.get(x, y)
                if len(cell) != 1:
                    return False
                if not (1 <= cell[0] <= 9):
                    return False

        # Check if solved.
        if not self.check():
            return False

        return True

    def remaining_cells(self):
        remaining = 0
        for x in range(9):
            for y in range(9):
                cell = self.get(x, y)
                if len(cell) > 1:
                    remaining += 1
        return remaining

    def remaining_space(self):
        space = 0
        for x in range(9):
            for y in range(9):
                cell = self.get(x, y)
                space += len(cell)
        space -= 81
        return space

    def display(self):
        if self.remaining_space() == 0:

            for row in self.matrix:
                for cell in row:
                    print(cell[0], end=' ')
                print()
            print()
        else:
            for row in self.matrix:
                for cell in row:
                    print(cell, end='\t')
                print()
            print()
