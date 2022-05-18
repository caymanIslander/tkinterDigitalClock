import imp
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")
#gets the time:
def time():
    string = strftime('%D:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
label = Label(root, background= "black", foreground="green")
label.pack(anchor='center')
time()

mainloop()