from tkinter import *
from tkinter.colorchooser import askcolor
import time, pickle

class Window(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.open_lower = Button(self, text='Pick lower color', command=self.pick_lower)
        self.open_upper = Button(self, text='Pick upper color', command=self.pick_upper)
        self.exit = Button(self, text='Go to Main', command=self.chamaMain)

        for b in (self.open_lower, self.open_upper, self.exit):
            b.pack(side=LEFT, expand=YES, fill=BOTH)
        self.pack()
    

    def chamaMain(self): import main

    def pick_lower(self):
        file = open('./data/list_lower.pkl', 'wb')
        selected_color = askcolor(parent=self, title='Select lower color')
        pickle.dump(selected_color[0][:3], file)
        file.close()

    def pick_upper(self):
        file = open('./data/list_upper.pkl', 'wb')
        selected_color = askcolor(parent=self, title='Select upper color')
        pickle.dump(selected_color[0][:3], file)
        file.close()

if __name__ == '__main__':
    win = Window(Tk())
    win.mainloop()