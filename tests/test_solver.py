from src.solver import solve, alg_eliminator  # , alg_select
from src.table_loader import Table_loader


def load_tables():
    loader = Table_loader()
    loader._load_tables()
    tables = [loader.get_table(index)[0] for index in range(50)]
    return tables


def test_solve():
    '''Very slow test!!'''
    solved = []

    for index, table in enumerate(load_tables()):
        assert not table.finished()
        table = solve(table)
        if table.finished():
            solved.append(index)
        else:
            # table.display()
            pass

    # assert len(solved) == 50
    assert len(solved) >= 12


def test_alg_eliminator():
    cell = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 003020600
    block = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [3],
             [1, 2, 3, 4, 5, 6, 7, 8, 9], [2], [1, 2, 3, 4, 5, 6, 7, 8, 9],
             [6], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]

    expected_cell = [1, 4, 5, 7, 8, 9]
    resulting_cell, changes = alg_eliminator(cell, block)
    assert changes == 3
    assert resulting_cell == expected_cell


def test_alg_select():
    pass
