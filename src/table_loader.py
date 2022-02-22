import os
import random
from src.sudoku_board import Sudoku_board


class Table_loader:
    def __init__(self, filename='sudoku_tables.txt'):
        folder = 'tables'
        self.path = os.path.join(folder, filename)
        self.tables = []

    def _load_tables(self):
        with open(self.path, 'r') as f:
            file_content = f.read()

        # Sort lines/text.
        table_contents = []
        current_table = ''
        for line in file_content.split('\n'):
            if line.startswith('Grid 01'):
                continue
            elif line.startswith('Grid '):
                table_contents.append(current_table)
                current_table = ''
            elif not line.startswith('Grid 01'):
                current_table += line + '\n'
        table_contents.append(current_table)

        # Parse text.
        self.tables = [self._generate_table(table) for table in table_contents]

    def _generate_table(self, grid_str):
        grid_list = grid_str.strip().split('\n')
        grid = []
        for line in grid_list:
            row = []
            for char in line:
                row.append(int(char))
            grid.append(row)
        return grid

    def __len__(self):
        return len(self.tables)

    def get_table(self, seed=None):
        '''If seed is not added, a random seed will be used.'''
        if seed is None:
            seed = random.randint(0, 49)

        board = Sudoku_board(self.tables[seed])
        return board, seed
