from lib import printer

class Sudoku_engine:
    board = [[]]
    matrix = [[[]]]


    def __inin__(self, board=None):
        if(board):
            self.board = board
        else:
            self.board = [[0 for _ in range(9)] for _ in range(9)]



    def solve(self, board):
        ## Empty 9x9x9 list: https://stackoverflow.com/questions/10668341/create-3d-array-using-python
        self.matrix = [[[0 for _ in range(9)] for _ in range(9)] for _ in range(9)]
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
                    # del self.matrix[x][y][:]
                    # self.matrix[x][y].append(board[x][y])



    def check(self, board):
        # Check if board is included
        if(board):
            self.board = board
        elif (not board and not self.board):
            print("No board")
            return False

        # Illegality check
        for x in range(9):
            for y in range(9):
                tmp = board[x][y]
                if(self.is_number(tmp)):
                    if(self.in_subgroup(x, y, tmp)):
                        #print("Illegal")
                        return False
        #print("Legal")

        # Completion check
        board_complete = True
        for x in range(9):
            for y in range(9):
                if (self.is_number(board[x][y])):
                    tmp = int(board[x][y])
                    if (not (tmp > 0 and tmp <= 9)):
                        board_complete = False
                else:
                    board_complete = False
        if(board_complete):
            print("Board complete")
        else:
            print("Board incomplete")

        return board_complete



    # If in subgroups: board is illegal
    def in_subgroup(self, x, y, num):
        if(int(num) == 0):
            return False

        sub_square = self.get_subgroup_square(x, y)
        sub_horizontal = self.get_subgroup_horizontal(x, y)
        sub_vertical = self.get_subgroup_vertical(x, y)

        #print((sub_square))
        #print((sub_horizontal))
        #print((sub_vertical))

        #sub_square = self.purge_empty(sub_square)
        #sub_horizontal= self.purge_empty(sub_horizontal)
        #sub_vertical= self.purge_empty(sub_vertical)

        if(not (len(sub_square) == 9 and len(sub_horizontal) == 9 and len(sub_vertical) == 9)):
            #print("Error in subgroup sized!")
            #return False
            pass

        num = int(num)
        def if_includes(lst):
            for i in range(len(lst)):
                #if(not i == exclude):
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
        #print(num)
        if(if_includes(sub_square)):
            print("[" + str(x+1) + "," + str(y+1) + "] includes sub-square illegality.")
            return True
        if (if_includes(sub_horizontal)):
            print("[" + str(x+1) + "," + str(y+1) + "] includes sub-horizontal illegality.")
            return True
        if (if_includes(sub_vertical)):
            print("[" + str(x+1) + "," + str(y+1) + "] includes sub-vertical illegality.")
            return True

        return False



    def purge_empty(self, lst):
        while '' in lst:
            lst.remove('')
        return lst



    def get_subgroup_square(self, x, y):
        #print(str(x) + " : " + str(y))
        sqX = self.get_square_coord(x)
        sqY = self.get_square_coord(y)
        #print(str(x) + " : " + str(y))
        #print(self.board)
        subgroup = []
        for j in range(3):
            for i in range(3):
                if(not (sqX+i == x and sqY+j == y)):
                    subgroup.append(self.board[sqX + i][sqY + j])

        #print(subgroup)
        return subgroup



    def get_square_coord(self, z):
        if(z >= 0 and z < 3):
            return 0
        elif(z >=3 and z < 6):
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
