#Buttom Lyout
from tkinter import ttk
from tkinter import *
root = Tk()
ttk.Button(root, text="vales verga").grid()
root.title("Feet to meters")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(coumn=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0,weight= 1)
mainframe.rowconfigure(0,weith=1)

feet = StringVar()
meters = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command="calculate").grid(column=3, row=3,
sticky=W)
root.mainloop()

