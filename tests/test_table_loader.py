from src.table_loader import Table_loader
from src.sudoku_board import Sudoku_board


def test_init():
    loader = Table_loader()
    assert type(loader) is Table_loader

    assert type(loader.path) is str
    assert loader.path == 'tables\\sudoku_tables.txt'

    assert type(loader.tables) is list
    assert len(loader.tables) == 0
    assert loader.tables == []


def test_load_tables():
    loader = Table_loader()
    assert type(loader.tables) is list
    assert len(loader.tables) == 0
    assert loader.tables == []

    loader._load_tables()
    assert type(loader.tables) is list
    assert len(loader.tables) == 50
    for table in loader.tables:
        assert type(table) is list
        assert len(table) == 9
        for row in table:
            assert type(row) is list
            assert len(row) == 9
            for cell in row:
                assert type(cell) is int
                assert 0 <= cell <= 9


def test_generate_table():
    table_str = '003020600\n900305001\n001806400\n' \
        + '008102900\n700000008\n006708200\n' \
        + '002609500\n800203009\n005010300'

    loader = Table_loader()
    table = loader._generate_table(table_str)

    assert type(table) is list
    assert len(table) == 9
    for row in table:
        assert type(row) is list
        assert len(row) == 9
        for cell in row:
            assert type(cell) is int
            assert 0 <= cell <= 9


def test_len_():
    loader = Table_loader()
    loader._load_tables()
    assert len(loader.tables) == 50
    assert len(loader) == 50
    loader.tables = loader.tables[:-1]
    assert len(loader) == 49


def test_get_table():
    # Set seed.
    seed = 3
    loader = Table_loader()
    loader._load_tables()
    table, used_seed = loader.get_table(seed)

    assert type(table) is Sudoku_board
    assert table.check()

    assert used_seed == seed == 3

    # Random seed.
    loader = Table_loader()
    loader._load_tables()

    seeds = []
    for i in range(10):
        table, used_seed = loader.get_table()
        seeds.append(used_seed)

        assert type(table) is Sudoku_board
        assert table.check()

    assert len(list(set(seeds))) > 1
