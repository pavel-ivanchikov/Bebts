import tkinter as tk
from tkinter import ttk

root = tk.Tk()

myframe_outer = ttk.Frame(root)
mycanvas = tk.Canvas(myframe_outer, height=20, width=300)
myframe_inner = ttk.Frame(mycanvas)
myscroll = ttk.Scrollbar(myframe_outer, orient='horizontal', command=mycanvas.xview)
mycanvas.configure(xscrollcommand=myscroll.set)

myframe_outer.grid()
mycanvas.grid(row=1, sticky='nesw')
myscroll.grid(row=2, sticky='ew')
mycanvas.create_window(0, 0, window=myframe_inner, anchor='nw')
ttk.Label(myframe_inner, text='test ' * 30).grid(sticky='w')

root.mainloop()