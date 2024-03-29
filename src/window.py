from src import file_interface as fInter
from src import sudoku_engine as engine
from src import printer

import tkinter as tk
import time


class Window:
    master = None
    board: list[list[int]] = [[]]
    orig_board: list[list[int]] = [[]]
    static_cells: list[int] = []
    entry_matrix: list[list[int]] = [[]]
    entry_IntVars: list[list[int]] = [[]]
    menu: list[int] = []
    indexing: list[int] = []
    size = 64
    start = 0

    timeVar = ""
    infoVar = ""

    running = True

    cell_position = [0, 0]

    # Color settings
    static_color = "#40E0D0"
    input_color = "#000000"
    error_color = "#FF0000"
    good_color = "#00FF00"

    x_square_color = "#EEE"
    diamond_square_color = "#FFF"

    tabFile = fInter.Table_file()
    suEng = engine.Sudoku_engine()

    def __init__(self, root_window):
        self.master = root_window

        w = (9 + 2 + 1) * self.size
        h = (9 + 1) * self.size
        shiftX = 200
        shiftY = 200
        geo = str(w) + "x" + str(h) + "+" + str(shiftX) + "+" + str(shiftY)

        root_window.geometry(geo)
        root_window.title("Sudoku Solver")

        # Numbering/indexing lines
        self.infoVar = tk.StringVar()
        self.indexing.append(tk.Label(root_window, textvariable=self.infoVar, font="Arial 12"))  # noqa
        self.indexing[0].place(x=0 * self.size, y=0 * self.size, width=self.size, height=self.size)  # noqa

        for i in range(9):
            self.indexing.append(tk.Label(root_window, text=str(i+1), font="Arial 24"))  # noqa
            self.indexing[i+1].place(x=(i+1) * self.size, y=0 * self.size, width=self.size, height=self.size)  # noqa

        for i in range(9):
            self.indexing.append(tk.Label(root_window, text=str(i+1), font="Arial 24"))  # noqa
            self.indexing[i+1+9].place(x=0 * self.size, y=(i+1) * self.size, width=self.size, height=self.size)  # noqa

        # Menu line
        self.timeVar = tk.StringVar()
        self.menu.append(tk.Label(root_window, textvariable=self.timeVar, font="Arial 24"))  # noqa
        self.menu[0].place(x=10 * self.size, y=0 * self.size, width=2 * self.size, height=self.size)  # noqa

        self.menu.append(tk.Button(root_window, text="New board", font="Arial 12", command=self.new_board))  # noqa
        self.menu[1].place(x=10 * self.size, y=1 * self.size, width=2 * self.size, height=self.size)  # noqa

        self.menu.append(tk.Button(root_window, text="New board\nfrom seed:", font="Arial 12", command=lambda: self.new_board([], self.menu[3].get())))  # noqa
        self.menu[2].place(x=10 * self.size, y=2 * self.size, width=2 * self.size, height=self.size)  # noqa

        self.menu.append(tk.Entry(root_window, justify="center", font="Arial 24"))  # noqa
        self.menu[3].place(x=10 * self.size, y=3 * self.size, width=2 * self.size, height=self.size)  # noqa

        self.menu.append(tk.Button(root_window, text="Check", font="Arial 12", command=self.board_check))  # noqa
        self.menu[4].place(x=10 * self.size, y=4 * self.size, width=2 * self.size, height=self.size)  # noqa

        self.menu.append(tk.Button(root_window, text="Solve", font="Arial 12", command=self.board_solve))  # noqa
        self.menu[5].place(x=10 * self.size, y=5 * self.size, width=2 * self.size, height=self.size)  # noqa

        self.menu.append(tk.Button(root_window, text="Reset", font="Arial 12", command=self.reset_board))  # noqa
        self.menu[6].place(x=10 * self.size, y=6 * self.size, width=2 * self.size, height=self.size)  # noqa

        self.menu.append(tk.Button(root_window, text="Save", font="Arial 12"))  # noqa
        self.menu[7].place(x=10 * self.size, y=7 * self.size, width=2 * self.size, height=self.size)  # noqa

        self.menu.append(tk.Button(root_window, text="Load", font="Arial 12"))  # noqa
        self.menu[8].place(x=10 * self.size, y=8 * self.size, width=2 * self.size, height=self.size)  # noqa

        self.menu.append(tk.Button(root_window, text="Settings", font="Arial 12"))  # noqa
        self.menu[9].place(x=10 * self.size, y=9 * self.size, width=2 * self.size, height=self.size)  # noqa

        table = []
        entry_vars = []
        for j in range(9):
            row = []
            entry_row = []
            for i in range(9):
                row.append(tk.Entry(root_window, justify="center", font="Arial 32 bold"))  # noqa
                row[i].place(x=(i+1)*self.size, y=(j+1)*self.size, width=self.size, height=self.size)  # noqa
                # row[j].grid(row=5*i, column=j, rowspan=5, columnspan=1)
                # Colours for sub-squares.
                # Part of x squares
                if(
                        (i < 3 and i >= 0 and j < 3 and j >= 0) or
                        (i < 6 and i >= 3 and j < 6 and j >= 3) or
                        (i < 9 and i >= 6 and j < 9 and j >= 6) or
                        (i < 3 and i >= 0 and j < 9 and j >= 6) or
                        (i < 9 and i >= 6 and j < 3 and j >= 0)
                ):
                    row[i].configure(background=self.x_square_color)
                # Part of diamond squares
                else:
                    row[i].configure(background=self.diamond_square_color)

                # name = str(i) + "," + str(j)
                # row[i].configure(name=name)
                # print(row[i].winfo_id())
                entry_row.append(tk.StringVar())
                # entry_row[i].trace("w", self.test())
            table.append(row)
            entry_vars.append(entry_row)
        self.entry_matrix = table
        self.entry_IntVars = entry_vars
        self.board = self.get_board()

    def update_cell(self, x, y, ins):
        self.entry_matrix[x][y].delete(0, 'end')
        self.entry_matrix[x][y].insert(0, str(ins))

    def get_cell(self, x, y):
        return self.entry_matrix[x][y].get()

    def get_board(self):
        table = []
        for x in range(9):
            row = []
            for y in range(9):
                row.append(self.get_cell(x, y))
            table.append(row)
        return table

    def set_board(self, board=None):
        for x in range(9):
            for y in range(9):
                self.update_cell(x, y, board[x][y])

    def clear_board(self, cell_input=""):
        for x in range(9):
            for y in range(9):
                self.update_cell(x, y, cell_input)
                self.entry_matrix[x][y].config(fg=self.input_color)

    def clean_board(self):
        for x in range(9):
            for y in range(9):
                cell = self.get_cell(x, y)
                if(cell):
                    if(self.is_number(cell)):
                        if(int(cell) > 0):
                            # if two numbers has been filled in.
                            if(int(cell) > 9):
                                return False
                            # Essentially return for this for-iteration
                            continue
                self.update_cell(x, y, "")
        return True

    def reset_board(self):
        self.new_board(self.orig_board)

    def new_board(self, matrix=None, seed=-1):
        if (not matrix):
            if (seed == -1):
                matrix = self.tabFile.get_table()
            elif (not self.is_number(seed)):
                print("Seed is not a number.")
                matrix = self.tabFile.get_table()
            else:
                matrix = self.tabFile.get_table(seed)

            """
            ##  Just no -_-
            ##  Simulated do while
            runs = 0
            not_done = True
            #while(not_done):
            while(runs < 5):
                print("run")
                if(seed == -1):
                    matrix = self.tabFile.get_table()
                elif(not self.is_number(seed)):
                    print("Seed is not a number.")
                    matrix = self.tabFile.get_table()
                else:
                    matrix = self.tabFile.get_table(seed)

                if (self.acceptable_board_size(matrix)):
                    continue

                runs += 1
                #if(not self.acceptable_board_size(matrix)):
                    #runs += 1
                    #not_done = False
            """

        self.clear_board()
        try:
            # Create board
            for x in range(9):
                for y in range(9):
                    if(self.is_number(matrix[x][y])):
                        num = int(matrix[x][y])
                        if(not num == 0):
                            self.update_cell(x, y, num)
                            self.entry_matrix[x][y].config(fg=self.static_color)  # noqa
        except (IndexError):
            # tabFile.get_table() probably returns a non-functional matrix.
            print("window.new_board() Index Error! Probably ignorable :P")
            return False

        self.orig_board = self.get_board()
        self.board = self.orig_board
        self.set_static_cells()
        self.reset_time()
        self.running = True
        self.update()
        return True

    def set_static_cells(self):
        # self.static_cells.clear()
        # del self.static_cells[:]
        self.static_cells = []
        for x in range(9):
            for y in range(9):
                cell = self.board[x][y]
                if(self.is_number(cell)):
                    cell = int(cell)
                    if(cell >= 1 and cell <= 9):
                        self.static_cells.append([x, y])

    def check_if_static(self, diff):
        if(diff in self.static_cells):
            return True
        return False

    def get_board_diff(self, board1, board2):
        for x in range(9):
            for y in range(9):
                if(not board1[x][y] == board2[x][y]):
                    return [x, y]
        return False

    def acceptable_board_size(self, board):
        if(not len(board) == 9):
            return False

        for x in range(9):
            if (not len(board[x]) == 9):
                return False

        # printer.printer(board)
        # print("---")
        return True

    def set_fg_color(self, x, y, color):
        self.entry_matrix[x][y].config(fg=color)

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

    def reset_time(self):
        self.start = time.time()
        pass

    def set_time(self):
        now = int(time.time() - self.start)

        mm = "00"
        ss = "00"
        mm = str(int(now / 60))
        ss = str(int(now % 60))

        if (int(mm) < 10):
            mm = "0" + mm
        if (int(ss) < 10):
            ss = "0" + ss

        formatted_now = mm + ":" + ss
        self.timeVar.set(formatted_now)

    def board_check(self):
        if(not self.suEng.legality_check(self.board)):
            # print("Illegal")
            self.infoVar.set(":(")
        else:
            self.infoVar.set(":)")

        if(self.suEng.completaion_check(self.board)):
            print("Board complete")
            self.infoVar.set(":D")
            self.running = False

    def board_solve(self):
        if(self.suEng.legality_check(self.board)):
            printer.printer(self.board)
            solved_board = self.suEng.solve(self.board)
            print("Solved board:")
            printer.printer(solved_board)
            for x in range(9):
                for y in range(9):
                    self.update_cell(x, y, solved_board[x][y])

    def board_update(self):
        # If change occured.
        if(not self.board == self.get_board()):
            # Create tmp board and backup board.
            tmp_board = self.get_board()
            backup_board = self.board

            # Get the changed cell.
            diff = self.get_board_diff(tmp_board, self.board)

            # If changed cell is not static cell.
            if(not self.check_if_static(diff)):
                self.board = tmp_board

                # If cell > 9 (i.e. two input numbers".
                if(not self.clean_board()):
                    # Reset self.board to backup_board and set as actual board.
                    self.board = backup_board
                    self.set_board(self.board)

                    # Make value in new cell by removing the previous number.
                    new_cell = tmp_board[diff[0]][diff[1]].replace(self.board[diff[0]][diff[1]], "")  # noqa

                    # Update cell (new_cell[], in case more than 2 numbers were put in). Exception is because stupid or something. -_-  # noqa
                    try:
                        self.update_cell(diff[0], diff[1], new_cell[len(new_cell) -1])  # noqa
                    except (IndexError):
                        self.update_cell(diff[0], diff[1], "")

            else:
                self.set_board(self.board)

            # self.suEng.legality_check(self.board)
            self.clean_board()
            self.board_check()

    def arrow_key_update(self, coord, plus):
        # If focus is on a cell, set cell_position to that cell.
        self.focus_entry_on_board()

        # Increment or decrement in x or y based on arrow key input.
        if(plus):
            self.cell_position[coord] += 1
        else:
            self.cell_position[coord] -= 1

        self.entry_matrix[self.cell_position[0]][self.cell_position[1]].focus()

    def focus_entry_on_board(self):
        # Focused << object that is focused on. Then chech if it exists, just in case? :P  # noqa
        focused = self.master.focus_get()
        if(not focused):
            return

        for x in range(9):
            for y in range(9):
                # If is of focused match id of cell at x,y.
                if(focused.winfo_id() == self.entry_matrix[x][y].winfo_id()):
                    self.cell_position = [x, y]

    def get_focus(self):
        # print(row[i].winfo_id())
        pass

    def update(self):
        if(self.running):
            self.set_time()
            self.board_update()

    # Key event functions
    def key_up(self, event):
        # print("Key pressed: up")
        # self.cell_position[0] += 1
        self.arrow_key_update(0, False)

    def key_down(self, event):
        # print("Key pressed: down")
        # self.cell_position[0] -= 1
        self.arrow_key_update(0, True)

    def key_left(self, event):
        # print("Key pressed: left")
        # self.cell_position[1] += 1
        self.arrow_key_update(1, False)

    def key_right(self, event):
        # print("Key pressed: right")
        # self.cell_position[1] -= 1
        self.arrow_key_update(1, True)

    def key_space(self, event):
        print("Key pressed: space")

    def key_enter(self, event):
        print("Key pressed: enter")
