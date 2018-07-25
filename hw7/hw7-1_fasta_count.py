# Problem 1
# Create a user friendly app that uses your function from last week's problem 1. Have the app include a file chooser.

from tkinter import *
from tkinter.filedialog import askopenfilename
import os, string


def fastaCount(filename):
    with open(filename, 'r') as f:
        count = 0
        line = f.readline()
        while line != '':
            if line.startswith('>'):
                count += 1
            line = f.readline()
    return count


class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        menubar = Menu(root)
        
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Open a file', command=self.select)
        filemenu.add_command(label='Quit', command=exit)
        menubar.add_cascade(label='File', menu=filemenu)

        master.config(menu=menubar)        
        
        Label(frame, font = ('arial', 16, 'bold'), text='Fasta file').grid(row=0, column=0)
        self.input_file = StringVar()
        self.input_name = StringVar()
        Label(frame, font = ('arial', 16, 'bold'), textvariable=self.input_name).grid(row=0, column=1)
        Label(frame, font = ('arial', 16, 'bold'), text='Number of sequences').grid(row=1, column=0)
        self.count = IntVar()
        Label(frame, font = ('arial', 16, 'bold'), textvariable=self.count).grid(row=1, column=1)
        Label(frame, font = ('arial', 14, 'bold'), fg = "blue", text='Press it to count ->').grid(row=2, column=0)

        button = Button(frame, padx = 16, pady = 16, bd = 8, fg = "black",
                          font = ('arial', 16, 'bold'), bg = "powder blue",
                          text='Count', command=self.counter)
        button.grid(row=2, column=1)

    def select(self):
        name = askopenfilename()
        self.input_name.set(os.path.split(name)[1])
        # Split the pathname path into a pair, (head, tail)
        # where tail is the last pathname component and head is everything leading up to that. 
        self.input_file.set(name)

    def counter(self):
        file = self.input_file.get()
        self.count.set(fastaCount(file))


root = Tk()
root.wm_title('Fasta Counter')
root.resizable(0, 0)
app = App(root)
root.mainloop()
