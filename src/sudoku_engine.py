# from src.printer import printer


class Sudoku_engine:
    board: list[list[int]] = [[]]
    matrix: list[list[list[int]]] = [[[]]]

    def __inin__(self, board=None):
        if(board):
            self.board = board
        else:
            self.board = [[0 for _ in range(9)] for _ in range(9)]

    def solve(self, board):
        self.generate_possibility_space_matrix(board)
        uncomplete = True
        while(uncomplete):
            # Check if list lengths are 1 for all cells.
            # (I.e. board is completed.)
            if(self.matrix_completion_check()):
                self.board = self.matrix_to_board()
                uncomplete = False
                continue

            # printer(self.matrix_length_board())
            # Iterate the eliminator algorithm (Method 1).
            if(not self.eliminator()):
                # Method 2
                pass
            # print("test  .")

        print("Board complete?")
        if(self.completaion_check(board)):
            print("Board complete!")
        else:
            print("Dafuq just happened!? o_O")

        return self.board

    def eliminator(self):
        # Repeating loop while changes happen.
        change_occured = True
        iterations = 0
        checks = 0  # Unnecessary, but fun.
        total_length = 0
        while(change_occured):  # Why u no dowhile, Python!?
            change_occured = False
            # Loop through matrix.
            for x in range(9):
                for y in range(9):
                    # Loop through possibility lists.
                    z = 0
                    total_length += len(self.matrix[x][y])
                    while(z < len(self.matrix[x][y])):
                        # for z in range(len(self.matrix[x][y])):
                        #    If element exists in subgroup (and is therefore not a possibility).  # noqa
                        # print(self.matrix[x][y][z])
                        if(self.in_subgroup(x, y, self.matrix[x][y][z])):
                            # Remove element from subgroup.
                            del self.matrix[x][y][z]
                            change_occured = True
                            # self.matrix[x][y].pop(z)
                            # print("Change occured")
                        else:
                            z += 1
                            # print("No change")
                        checks += 1
            iterations += 1
            # print("test  -")
            # print("Iteration: " + str(iterations))
        # print("Total length: " + str(total_length))
        # print("Total iterations: " + str(iterations) + "\t- Total checks: " + str(checks))  # noqa
        return change_occured

    def matrix_to_board(self):
        board = [[0 for _ in range(9)] for _ in range(9)]
        for x in range(9):
            for y in range(9):
                board[x][y] = self.matrix[x][y][0]
        return board

    def matrix_length_board(self):
        board = [[0 for _ in range(9)] for _ in range(9)]
        for x in range(9):
            for y in range(9):
                board[x][y] = len(self.matrix[x][y])
        return board

    def matrix_completion_check(self):
        total_list_lengths = 0
        ones = 0
        for x in range(9):
            for y in range(9):
                total_list_lengths += len(self.matrix[x][y])
                if(not len(self.matrix[x][y]) == 1):
                    # print("Still not complete")
                    return False
                elif(not len(self.matrix[x][y]) >= 1):
                    print("Empty list")
                else:
                    ones += 1
        # print(ones)
        print("List lengths: " + str(total_list_lengths))
        return True

    def generate_possibility_space_matrix(self, board):
        # Create the matrix possibility space
        # Empty 9x9x9 list:
        # https://stackoverflow.com/questions/10668341/create-3d-array-using-python  # noqa
        self.matrix = [[[] for _ in range(9)] for _ in range(9)]
        # print(self.matrix)
        for x in range(9):
            for y in range(9):
                cell = board[x][y]
                # If cell has value
                if (self.is_number(cell)):
                    cell = int(cell)
                    # If cell is acceptable number
                    if (cell > 0 and cell <= 9):
                        self.matrix[x][y] = [cell]
                        continue
                for z in range(9):
                    self.matrix[x][y].append(z)
        # print(self.matrix)

    def legality_check(self, board):
        self.board = board
        for x in range(9):
            for y in range(9):
                tmp = board[x][y]
                if(self.is_number(tmp)):
                    if(self.in_subgroup(x, y, tmp)):
                        return False
        return True

    def completaion_check(self, board):
        self.board = board
        for x in range(9):
            for y in range(9):
                if (self.is_number(board[x][y])):
                    tmp = int(board[x][y])
                    if (tmp > 0 and tmp <= 9):
                        continue
                return False
        return True

    # If in subgroups: board is illegal
    def in_subgroup(self, x, y, num):
        if(int(num) == 0):
            return False

        sub_square = self.get_subgroup_square(x, y)
        sub_horizontal = self.get_subgroup_horizontal(x, y)
        sub_vertical = self.get_subgroup_vertical(x, y)

        # print((sub_square))
        # print((sub_horizontal))
        # print((sub_vertical))

        # sub_square = self.purge_empty(sub_square)
        # sub_horizontal= self.purge_empty(sub_horizontal)
        # sub_vertical= self.purge_empty(sub_vertical)

        if(not (len(sub_square) == 9-1
                and len(sub_horizontal) == 9-1
                and len(sub_vertical) == 9-1)):
            # print("Error in subgroup sized!")
            # return False
            pass

        num = int(num)

        def if_includes(lst):
            for i in range(len(lst)):
                # if(not i == exclude):
                if(self.is_number(lst[i])):
                    if(num == int(lst[i])):
                        return True
            return False
        """
        if(num > 0 and num < 10):
            print("num: " + str(num))
            for i in range(9):
                print(sub_square[i])
                print(sub_horizontal[i])
                print(sub_vertical[i])
        """
        # print(num)
        if(if_includes(sub_square)):
            # print("Illegal: Cell [" + str(x+1) + "," + str(y+1) + "] includes sub-square illegality.")  # noqa
            return True
        if (if_includes(sub_horizontal)):
            # print("Illegal: Cell [" + str(x+1) + "," + str(y+1) + "] includes sub-horizontal illegality.")  # noqa
            return True
        if (if_includes(sub_vertical)):
            # print("Illegal: Cell [" + str(x+1) + "," + str(y+1) + "] includes sub-vertical illegality.")  # noqa
            return True

        return False

    def purge_empty(self, lst):
        while '' in lst:
            lst.remove('')
        return lst

    def get_subgroup_square(self, x, y):
        # print(str(x) + " : " + str(y))
        sqX = self.get_square_coord(x)
        sqY = self.get_square_coord(y)
        # print(str(x) + " : " + str(y))
        # print(self.board)
        subgroup = []
        for j in range(3):
            for i in range(3):
                if(not (sqX+i == x and sqY+j == y)):
                    subgroup.append(self.board[sqX + i][sqY + j])

        # print(subgroup)
        return subgroup

    def get_square_coord(self, z):
        if(z >= 0 and z < 3):
            return 0
        elif(z >= 3 and z < 6):
            return 3
        elif(z >= 6 and z < 9):
            return 6
        else:
            print("Coordinate error!")

    def get_subgroup_horizontal(self, x, y):
        subgroup = []
        for i in range(9):
            if(not i == x):
                subgroup.append(self.board[i][y])
        return subgroup

    def get_subgroup_vertical(self, x, y):
        subgroup = []
        for j in range(9):
            if(not j == y):
                subgroup.append(self.board[x][j])
        return subgroup

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False
