from src import file_interface as fInter
from src import printer
from src import window



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

# Key bindings: http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
root_window.bind('<Up>', win.key_up)
root_window.bind('<Down>', win.key_down)
root_window.bind('<Left>', win.key_left)
root_window.bind('<Right>', win.key_right)
root_window.bind('<space>', win.key_space)
root_window.bind('<Return>', win.key_enter)


root_window.after(100, update)
root_window.mainloop()
