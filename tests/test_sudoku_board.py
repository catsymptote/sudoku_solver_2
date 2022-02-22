from src.sudoku_board import Sudoku_board
from src.solver import solve


def get_new_table():
    table = ['003020600',
             '900305001',
             '001806400',
             '008102900',
             '700000008',
             '006708200',
             '002609500',
             '800203009',
             '005010300']

    for row_idx, row in enumerate(table):
        row = list(row)
        row_list = []
        for cell in row:
            row_list.append(int(cell))
        table[row_idx] = row_list
    return table


def test_get_new_table():
    table = get_new_table()
    assert type(table) is list
    assert len(table) == 9
    for row in table:
        assert type(row) is list
        assert len(row) == 9
        for cell in row:
            assert type(cell) is int
            assert 0 <= cell <= 9


def test_init():
    board = Sudoku_board()
    assert type(board) is Sudoku_board

    assert len(board.matrix) == 9
    for row in board.matrix:
        assert type(row) == list
        assert len(row) == 9
        for column in row:
            assert type(column) == list
            assert len(column) == 9
            for idx, item in enumerate(column):
                assert idx + 1 == item


def test_init_from_table():
    table = get_new_table()
    board = Sudoku_board(table)
    assert type(board) is Sudoku_board


def test_at():
    board = Sudoku_board(get_new_table())
    assert board.get(0, 2) == [3]

    lst = list(range(1, 10))

    assert board.get(0, 0, 'row') == [lst, lst, [3], lst, [2], lst, [6], lst, lst]  # noqa
    assert board.get(3, 0, 'row') == [lst, lst, [8], [1], lst, [2], [9], lst, lst]  # noqa

    assert board.get(0, 0, 'col') == [lst, [9], lst, lst, [7], lst, lst, [8], lst]  # noqa
    assert board.get(0, 3, 'col') == [lst, [3], [8], [1], lst, [7], [6], [2], lst]  # noqa

    assert board.get(0, 0, 'sqr') == [lst, lst, [3], [9], lst, lst, lst, lst, [1]]  # noqa
    assert board.get(0, 3, 'sqr') == [lst, [2], lst, [3], lst, [5], [8], lst, [6]]  # noqa


def test_set_cell():
    board = Sudoku_board(get_new_table())
    assert board.get(0, 2) == [3]
    assert board.get(0, 0) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    board.set_cell(0, 0, [1, 2, 3])
    assert board.get(0, 0) == [1, 2, 3]


def test_check():
    board = Sudoku_board(get_new_table())
    assert board.check()
    board.matrix[1][1] = [3]
    board.matrix[0][0] = [8]
    assert not board.check()


def test_finished():
    board = Sudoku_board(get_new_table())
    assert not board.finished()
    board = solve(board)
    assert board.finished()
