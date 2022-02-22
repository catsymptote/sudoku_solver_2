def solve(board):
    runs = 0

    changed = True
    while not board.finished() and runs < 100 and changed:
        changed = False
        for x in range(9):
            for y in range(9):
                for tag in ['row', 'column', 'square']:
                    for alg in [alg_eliminator]:
                        block = board.get(x, y, tag)
                        cell = board.get(x, y)
                        cell, changes = alg(cell, block)
                        board.set_cell(x, y, cell)
                        if changes > 0:
                            changed = True

        runs += 1

    # print(board.finished(), board.check(), runs, changed, board.remaining_cells(), board.remaining_space())  # noqa
    return board


def alg_eliminator(cell1, block):
    '''Do a simple elimination process on the board possibilities.
    If cell2 if N, then cell1 cannot be N, and N can therefore be removed.'''
    changes = 0

    for cell2 in block:
        if len(cell1) == 1:
            return cell1, changes

        elif len(cell2) == 1:
            value = cell2[0]
            if value in cell1:
                cell1.remove(value)
                changes += 1

    return cell1, changes


def alg_select(cell1, block):
    '''If cell1 is the only cell in the block, which has N,
    then cell1 has to be N.

    DISCARDED! Does the same thing as eliminator.'''
    changes = 0

    for value in cell1:
        if len(cell1) == 1:
            return cell1, changes

        value_count = 0
        for cell2 in block:
            value_count += cell2.count(value)

        if value_count == 1:
            cell1 = [value]
        changes += 1

    return cell1, changes
