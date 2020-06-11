from tkinter import *
import random

master = Tk()

def clicked_point(event):
    pass

def clicked_start(event):
    x_coord = 0
    y_coord = 0
    dot = canvas1.create_oval(0,0, 50, 50, fill="red", tags="point")
    canvas1.tag_bind("point", "<Button-1>", clicked_point)

def clicked_end(event):
    pass

canvas1 = Canvas(master, width=1000, height=1000)
canvas1.pack()

