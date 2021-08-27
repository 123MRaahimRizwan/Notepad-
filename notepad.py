from tkinter import *
from tkinter import messagebox, filedialog
import os

def create_widgets():
    global textarea

    textarea = Text(root)
    textarea.grid(sticky=N+E+W+S)


    menubar = Menu(root)
    root.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label='New', command=newfile)
    filemenu.add_command(label='Open', command=openfile)
    filemenu.add_command(label='Save', command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=exit)
    menubar.add_cascade(label='File', menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label='Cut', command=cut)
    editmenu.add_command(label='Copy', command=copy)
    editmenu.add_command(label='Paste', command=paste)
    menubar.add_cascade(label='Edit', menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label='About Notepad', command=help)
    menubar.add_cascade(label="Help", menu=helpmenu )



def newfile():
    global textarea
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)

def openfile():
    global textarea
    file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text documents", "*.txt")])
    file = file.name
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file + " - Notepad"))
        textarea.delete(1.0, END)
        file = open(file, 'rb')
        textarea.insert(1.0, file.read())
        file.close()

def savefile():
    global textarea, file
    if file == None:
        file = filedialog.asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text documents", "*.txt")])
        if file == None:
            file = None
        else:
            file = open(file, 'w')
            file.write(textarea.get(1.0, END))
            file.close()
            file = file.name
            root.title(os.path.basename(file) + ' - Notepad')

    else:
        file = open(file, 'w')
        file.write(textarea.get(1.0, END))
        file.close()

def exit():
    root.destroy()

def cut():
    global textarea
    textarea.event_generate("<<Cut>>")
def copy():
    global textarea
    textarea.event_generate("<<Copy>>")
def paste():
    global textarea
    textarea.event_generate("<<Paste>>")

def help():
    messagebox.showinfo("Notepad", "This is a notepad made by M.Raahim Rizwan.")


root = Tk()
root.wm_iconbitmap('icon.ico')
root.title('Untitled - Notepad')
file = None

create_widgets()

root.mainloop()

