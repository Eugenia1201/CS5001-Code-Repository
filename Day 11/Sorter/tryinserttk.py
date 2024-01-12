"""Try TKinter Canvas for display of list of rectangles."""

import tkinter as tk
import tkinter.ttk as ttk
import random
import time

MAX_NUMBER = 100
LIST_LENGTH = 25

FRAME_WIDTH = 800
X_MARGIN = 50
X_SCALE = (FRAME_WIDTH - (X_MARGIN + X_MARGIN)) / LIST_LENGTH
X_SPACE = 2

FRAME_HEIGHT = 600
Y_MARGIN = 50
Y_SCALE = (FRAME_HEIGHT - (Y_MARGIN + Y_MARGIN)) / MAX_NUMBER


class ListFrame(tk.Canvas):
    """Display a rectangle list on a Canvas."""

    def __init__(self, master):
        """Initialize the Canvas."""
        super().__init__(master, width=FRAME_WIDTH, height=FRAME_HEIGHT,
                         bg="white")
        self.number_list = None
        self.rectangle_list = None

    def setup(self, number_list):
        """Set up a new number list and its rectangle display."""
        self.number_list = number_list
        if self.rectangle_list is not None:
            for r in self.rectangle_list:
                self.delete(r)
        self.rectangle_list = []
        for i in range(len(self.number_list)):
            r = self.setup_rectangle(i)
            self.rectangle_list.append(r)

    def setup_rectangle(self, i):
        """Set up one Rectangle."""
        left = X_MARGIN + (i * X_SCALE)
        right = X_MARGIN + (i * X_SCALE) + X_SCALE - X_SPACE
        top = FRAME_HEIGHT - (Y_MARGIN + (self.number_list[i] * Y_SCALE))
        bottom = FRAME_HEIGHT - Y_MARGIN
        r = self.create_rectangle(left, top, right, bottom, fill="skyblue",
                                  outline="")
        return r

    def sort(self):
        """Sort the number list while updating display."""
        for r in self.rectangle_list:
            self.set_color(r, "skyblue")
        self.set_color(self.rectangle_list[0], "green")
        root.update_idletasks()
        for i in range(1, LIST_LENGTH):
            this_rectangle = self.rectangle_list[i]
            self.set_color(this_rectangle, "red")
            root.update_idletasks()
            if fast_q.get():
                time.sleep(0.1)
            else:
                time.sleep(0.6)
            for j in range(i, 0, -1):
                if self.number_list[j] > self.number_list[j-1]:
                    break
                display.swap(j-1, j)
                self.number_list[j], self.number_list[j-1] =\
                    self.number_list[j-1], self.number_list[j]
                root.update_idletasks()
                if fast_q.get():
                    time.sleep(0.05)
                else:
                    time.sleep(0.25)
            self.set_color(this_rectangle, "green")

    def swap(self, i, j):
        """Swap two rectangles."""
        self.move(self.rectangle_list[i], X_SCALE, 0)
        self.move(self.rectangle_list[j], -X_SCALE, 0)
        self.rectangle_list[i], self.rectangle_list[j] =\
            self.rectangle_list[j], self.rectangle_list[i]

    def set_color(self, r, color):
        """Set the color of a given rectangle."""
        self.itemconfig(r, fill=color)


def on_setup():
    """Set up new number list."""
    number_list = [random.randint(1, MAX_NUMBER) for i in range(LIST_LENGTH)]
    display.setup(number_list)
    sort_button["state"] = "normal"


def on_sort():
    """Sort the number list."""
    display.sort()


def on_quit():
    """Quit the program."""
    exit()


if __name__ == "__main__":

    root = tk.Tk()

    control_frame = ttk.Frame(root)
    control_frame.grid(row=0, column=0)
    setup_button = ttk.Button(control_frame, text="Setup", command=on_setup)
    setup_button.grid(row=0, column=0)
    sort_button = ttk.Button(control_frame, text="Sort", command=on_sort)
    sort_button["state"] = "disabled"
    sort_button.grid(row=1, column=0)
    quit_button = ttk.Button(control_frame, text="Quit", command=on_quit)
    quit_button.grid(row=2, column=0)
    fast_q = tk.IntVar()
    fast_checkbox = ttk.Checkbutton(control_frame, text="Fast?",
                                    variable=fast_q)
    fast_checkbox.grid(row=3, column=0)

    display = ListFrame(root)
    display.grid(row=0, column=1)

    root.mainloop()
