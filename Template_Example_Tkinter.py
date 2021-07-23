import sys
import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("116x72")
label = ttk.Label(text=u'Label')
label.pack()
Button = ttk.Button(text=u'Push Button')
Button.pack()

root.mainloop()