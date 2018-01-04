from lib import file_interface as fInter
from lib import printer
from lib import window



import tkinter as tk


root_window = tk.Tk()

tabFile = fInter.Table_file()
win = window.Window(root_window)
#printer.printer(tabFile.get_table(3))

win.update_cell(0, 0, "a")
win.update_cell(0, 0, 0)
win.update_cell(1, 6, 0)

win.clear_board()

win.new_board(tabFile.get_random_table())


#print(win.get_board())

def update():
    win.update()
    root_window.after(100, update)

root_window.after(100, update)
root_window.mainloop()
