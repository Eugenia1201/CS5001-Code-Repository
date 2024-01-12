"""TK display of sorting."""

import tkinter as tk
import tkinter.ttk as ttk
import random
import time

import btreesorter as sorter


FRAME_WIDTH = 800
X_MARGIN = 50
X_SPACE = 1

FRAME_HEIGHT = 600
Y_MARGIN = 50

DISPLAY_LIMIT = 200


class ListFrame(tk.Canvas):
    """Display a rectangle list on a Canvas."""

    def __init__(self, master):
        """Initialize the Canvas."""
        super().__init__(master, width=FRAME_WIDTH, height=FRAME_HEIGHT,
                         bg="white")
        self.rectangle_list = None
        self.x_scale = None
        self.y_scale = None

    def display(self, number_list, max_number):
        """Set up a new number list and its rectangle display."""
        # clear any currently displayed rectangles
        if self.rectangle_list is not None:
            for r in self.rectangle_list:
                self.delete(r)
        # set up the new display
        if len(number_list) <= DISPLAY_LIMIT:
            x_scale = (FRAME_WIDTH - (X_MARGIN + X_MARGIN)) / len(number_list)
            y_scale = (FRAME_HEIGHT - (Y_MARGIN + Y_MARGIN)) / max_number
            self.rectangle_list = []
            for i in range(len(number_list)):
                r = self.setup_rectangle(i, number_list[i], x_scale, y_scale)
                self.rectangle_list.append(r)
        else:
            self.rectangle_list = None
        root.update_idletasks()

    def setup_rectangle(self, i, value_i, x_scale, y_scale):
        """Set up one Rectangle."""
        left = X_MARGIN + (i * x_scale)
        right = X_MARGIN + (i * x_scale) + x_scale - X_SPACE
        top = FRAME_HEIGHT - (Y_MARGIN + (value_i * y_scale))
        bottom = FRAME_HEIGHT - Y_MARGIN
        r = self.create_rectangle(left, top, right, bottom, fill="skyblue",
                                  outline="")
        return r


def on_setup():
    """Create a new number list and display it."""
    global max_number, number_list
    """Set up new number list."""
    list_length = list_length_v.get()
    max_number = max_number_v.get()

    number_list = [random.randint(1, max_number) for i in range(list_length)]
    display.display(number_list, max_number)
    sort_button["state"] = "normal"


def on_sort():
    """Sort the number list."""
    global max_number, number_list, fast_q
    fast_q = fast_v.get() or (len(number_list) > DISPLAY_LIMIT)

    setup_button["state"] = "disabled"
    sort_button["state"] = "disabled"
    quit_button["state"] = "disabled"
    fast_checkbox["state"] = "disabled"
    list_length_entry["state"] = "disabled"
    max_number_entry["state"] = "disabled"

    # HERE WE CALL THE SORT FUNCTION
    elapsed_time, result_list = sorter.sort_list(number_list, on_display)

    display.display(result_list, max_number)
    elapsed_time_label.config(text=f"Elapsed time: {elapsed_time}")
    number_list = result_list

    setup_button["state"] = "normal"
    sort_button["state"] = "normal"
    quit_button["state"] = "normal"
    fast_checkbox["state"] = "normal"
    list_length_entry["state"] = "normal"
    max_number_entry["state"] = "normal"


def on_display(sorted_list):
    """Update the display after a step of sorting."""
    global max_number, fast_q
    if not fast_q:
        time.sleep(0.5)
    display.display(sorted_list, max_number)


def on_quit():
    """Quit the program."""
    exit()


if __name__ == "__main__":

    root = tk.Tk()

    control_frame = ttk.Frame(root)
    control_frame.grid(row=0, column=0)

    ttk.Label(control_frame, text=sorter.sort_name)\
        .grid(row=0, column=0, columnspan=2)

    parameters_frame = ttk.Frame(control_frame)
    parameters_frame.grid(row=2, column=0)
    list_length_v = tk.IntVar(value=25)
    ttk.Label(parameters_frame, text="List Length:").grid(row=0, column=0)
    list_length_entry = ttk.Entry(parameters_frame, textvariable=list_length_v)
    list_length_entry.grid(row=0, column=1)
    max_number_v = tk.IntVar(value=100)
    ttk.Label(parameters_frame, text="Max Value: ")\
        .grid(row=1, column=0)
    max_number_entry = ttk.Entry(parameters_frame, textvariable=max_number_v)
    max_number_entry.grid(row=1, column=1)
    fast_v = tk.IntVar()
    fast_checkbox = ttk.Checkbutton(parameters_frame, text="Fast?",
                                    variable=fast_v)
    fast_checkbox.grid(row=2, column=0)

    elapsed_time_label = ttk.Label(control_frame)
    elapsed_time_label.grid(row=3, column=0)
    setup_button = ttk.Button(control_frame, text="Setup", command=on_setup)
    setup_button.grid(row=5, column=0)
    sort_button = ttk.Button(control_frame, text="Sort", command=on_sort)
    sort_button["state"] = "disabled"
    sort_button.grid(row=6, column=0)
    quit_button = ttk.Button(control_frame, text="Quit", command=on_quit)
    quit_button.grid(row=7, column=0)

    display = ListFrame(root)
    display.grid(row=0, column=1)

    root.mainloop()
