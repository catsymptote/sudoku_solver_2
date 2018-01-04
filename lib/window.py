from lib import file_interface as fInter
from lib import sudoku_engine as engine


import tkinter as tk
import time



class Window:
    board = [[]]
    entry_matrix = [[]]
    entry_IntVars = [[]]
    menu = []
    size = 64
    start = 0

    timeVar = ""




    # Color settings
    static_color    = "#40E0D0"
    input_color     = "#000000"
    error_color     = "#FF0000"
    good_color      = "#00FF00"


    tabFile = fInter.Table_file()
    suEng = engine.Sudoku_engine()


    def __init__(self, root_window):
        w = (9 + 2) * self.size
        h = (9) * self.size
        shiftX = 200
        shiftY = 200
        geo = str(w) + "x" + str(h) + "+" + str(shiftX) + "+" + str(shiftY)


        root_window.geometry(geo)
        root_window.title("Sudoku Solver")



        self.timeVar = tk.StringVar()

        self.menu.append(tk.Label(root_window, textvariable=self.timeVar, font="Arial 24"))
        self.menu[0].place(x=9 * self.size, y=0 * self.size, width=2 * self.size, height=self.size)

        self.menu.append(tk.Button(root_window, text="New board", font="Arial 12", command=self.new_board))
        self.menu[1].place(x=9 * self.size, y=1 * self.size, width=2 * self.size, height=self.size)

        self.menu.append(tk.Button(root_window, text="New board\nfrom seed:", font="Arial 12", command=lambda: self.new_board([], self.menu[3].get())))
        self.menu[2].place(x=9 * self.size, y=2 * self.size, width=2 * self.size, height=self.size)

        self.menu.append(tk.Entry(root_window, justify="center", font="Arial 24"))
        self.menu[3].place(x=9 * self.size, y=3 * self.size, width=2 * self.size, height=self.size)

        self.menu.append(tk.Button(root_window, text="Check", font="Arial 12", command=lambda: self.suEng.check(self.board)))
        self.menu[4].place(x=9 * self.size, y=4 * self.size, width=2 * self.size, height=self.size)

        self.menu.append(tk.Button(root_window, text="Solve", font="Arial 12"))
        self.menu[5].place(x=9 * self.size, y=5 * self.size, width=2 * self.size, height=self.size)

        self.menu.append(tk.Button(root_window, text="Save", font="Arial 12"))
        self.menu[6].place(x=9 * self.size, y=6 * self.size, width=2 * self.size, height=self.size)

        self.menu.append(tk.Button(root_window, text="Load", font="Arial 12"))
        self.menu[7].place(x=9 * self.size, y=7 * self.size, width=2 * self.size, height=self.size)

        self.menu.append(tk.Button(root_window, text="Settings", font="Arial 12"))
        self.menu[8].place(x=9 * self.size, y=8 * self.size, width=2 * self.size, height=self.size)




        table = []
        entry_vars = []
        for i in range(9):
            row = []
            entry_row = []
            for j in range(9):
                row.append(tk.Entry(root_window, justify="center", font="Arial 32 bold"))
                row[j].place(x=i*self.size, y=j*self.size, width=self.size, height=self.size)
                #row[j].grid(row=5*i, column=j, rowspan=5, columnspan=1)

                entry_row.append(tk.StringVar())
                entry_row[j].trace("w", self.test())
            table.append(row)
            entry_vars.append(entry_row)
        self.entry_matrix = table
        self.entry_IntVars = entry_vars
        self.board = self.get_board()



    def update_cell(self, x, y, ins):
        self.entry_matrix[x][y].delete(0)
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



    def clear_board(self, cell_input = ""):
        for x in range(9):
            for y in range(9):
                self.update_cell(x, y, cell_input)



    def new_board(self, matrix=[], seed=-1):
        if(not matrix):
            # No seed
            if(seed == -1):
                matrix = self.tabFile.get_table()
            elif(not self.is_number(seed)):
                print("Seed is not a number.")
                matrix = self.tabFile.get_table()
            else:
                matrix = self.tabFile.get_table(seed)

        self.clear_board()

        for x in range(9):
            for y in range(9):
                if(self.is_number(matrix[x][y])):
                    num = int(matrix[x][y])
                    if(not num == 0):
                        self.update_cell(x, y, num)
                        self.entry_matrix[x][y].config(fg=self.static_color)

        self.reset_time()
        self.update()



    def set_fg_color(self, x, y, color):
        self.entry_matrix[x][y].config(fg=self.color)



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



    def board_update(self):
        if(not self.board == self.get_board()):
            self.suEng.check(self.board)
            print("Changes found.")
        self.board = self.get_board()




    def test(self, *args):
        #print("test")
        pass



    def update(self):
        self.set_time()
        self.board_update()
