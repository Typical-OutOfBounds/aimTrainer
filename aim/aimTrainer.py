from tkinter import *
import random
import time
import serial

class Trainer:
    def __init__(self):
        self.master = Tk()
        self.canvas1 = Canvas(self.master, width=1000, height=1000)
        self.canvas1.pack()

        self.start = Button(self.master, text="Start")
        self.start.configure(width=10)
        self.start.bind('<Button-1>', self.clicked_start)
        self.start_window = self.canvas1.create_window(10, 10, anchor=NW, window=self.start)

        self.end = Button(self.master, text="End")
        self.end.configure(width=10)
        self.end.bind('<Button-1>', self.clicked_end)
        self.end_window = self.canvas1.create_window(10, 50, anchor=NW, window=self.end)

        self.counter = 0

    def clicked_point(self, event):
        if time.perf_counter() - self.counter > 5:
            with serial.Serial('COM3', 9600, timeout=1) as ser:
                ser.write(str.encode('H'))
                time.sleep(2)
                ser.write(str.encode('L'))
            self.master.destroy()
        else:
            self.counter = time.perf_counter()
            self.canvas1.delete(self.dot)
            x_coord = random.randint(10, 990)
            y_coord = random.randint(10, 990)
            self.dot = self.canvas1.create_oval(x_coord, y_coord, x_coord + 30, y_coord + 30, fill="red", tags="point")
            self.canvas1.tag_bind("point", "<Button-1>", self.clicked_point)

    def clicked_start(self, event):
        x_coord = random.randint(10, 990)
        y_coord = random.randint(10, 990)
        self.dot = self.canvas1.create_oval(x_coord, y_coord, x_coord + 30, y_coord + 30, fill="red", tags="pointFirst")
        self.canvas1.tag_bind("pointFirst", "<Button-1>", self.clicked_point)

    def clicked_end(self, event):
        self.master.destroy()


myTrainer = Trainer()
myTrainer.master.mainloop()

# master = Tk()
#
#
#
# canvas1 = Canvas(master, width=1000, height=1000)
# canvas1.pack()
#
# start = Button(master, text="Start")
# start.configure(width=10)
# start.bind('<Button-1>', clicked_start)
# start_window = canvas1.create_window(10, 10, anchor=NW, window=start)
#
# master.mainloop()