"""CS 5001 - Kaiqi Zhang - Project 9 'Into the Forest' - 18 Nov
"""
import forestconfig
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkbox
import jsonpickle

# instantiate global variables
root = tk.Tk()
global config


class App:
    """
    Represents the main application for running the forest simulation.

    Attributes:
        None

    Methods:
        run():Runs the forest simulation application.
    """

    def __init__(self):
        """
        Initialize the App object.
        """
        root.title("Into The Forest")
        my_frame = ttk.Frame(root, padding=10)
        my_frame.grid()
        ttk.Label(my_frame, text="Minimum number of kids:").grid(
            row=0, column=0)
        ttk.Label(my_frame, text="Maximum number of kids:").grid(
            row=1, column=0)
        ttk.Label(my_frame, text="Minimum size of kids:").grid(
            row=2, column=0)
        ttk.Label(my_frame, text="Maximum size of kids:").grid(
            row=3, column=0)
        ttk.Label(my_frame, text="Minimum number of trees:").grid(
            row=4, column=0)
        ttk.Label(my_frame, text="Maximum numbers of trees:").grid(
            row=5, column=0)
        ttk.Label(my_frame, text="Minimum size of trees:").grid(
            row=6, column=0)
        ttk.Label(my_frame, text="Maximum size of trees:").grid(
            row=7, column=0)
        ttk.Label(my_frame, text="Minimum number of flyers:").grid(
            row=8, column=0)
        ttk.Label(my_frame, text="Maximum number of flyers:").grid(
            row=9, column=0)
        ttk.Label(my_frame, text="Minimum size of flyers:").grid(
            row=10, column=0)
        ttk.Label(my_frame, text="Maximum size of flyers:").grid(
            row=11, column=0)

        ttk.Button(my_frame, text="Save",
                   command=self.on_start).grid(row=12, column=0)

        self.nkids_min = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.nkids_min).grid(row=0, column=1)
        self.nkids_max = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.nkids_max).grid(row=1, column=1)
        self.kids_size_min = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.kids_size_min).grid(row=2,
                                                                  column=1)
        self.kids_size_max = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.kids_size_max).grid(row=3,
                                                                  column=1)
        self.ntrees_min = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.ntrees_min).grid(row=4, column=1)
        self.ntrees_max = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.ntrees_max).grid(row=5, column=1)
        self.trees_size_min = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.trees_size_min).grid(row=6,
                                                                   column=1)
        self.trees_size_max = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.trees_size_max).grid(row=7,
                                                                   column=1)
        self.nflyers_min = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.nflyers_min).grid(row=8,
                                                                column=1)
        self.nflyers_max = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.nflyers_max).grid(row=9,
                                                                column=1)
        self.flyers_size_min = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.flyers_size_min).grid(row=10,
                                                                    column=1)
        self.flyers_size_max = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.flyers_size_max).grid(row=11,
                                                                    column=1)

    def on_start(self):
        """Convert user input into strings, validate input values,
        and set up the configuration using these values."""
        config_number_strings = []
        config_size_strings = []
        config_numbers = []
        config_sizes = []

        # get string value out of each StringVar object
        nkids_min_input = self.nkids_min.get()
        config_number_strings.append(nkids_min_input)
        nkids_max_input = self.nkids_max.get()
        config_number_strings.append(nkids_max_input)
        kids_size_min_input = self.kids_size_min.get()
        config_size_strings.append(kids_size_min_input)
        kids_size_max_input = self.kids_size_max.get()
        config_size_strings.append(kids_size_max_input)
        ntrees_min_input = self.ntrees_min.get()
        config_number_strings.append(ntrees_min_input)
        ntrees_max_input = self.ntrees_max.get()
        config_number_strings.append(ntrees_max_input)
        trees_size_min_input = self.trees_size_min.get()
        config_size_strings.append(trees_size_min_input)
        trees_size_max_input = self.trees_size_max.get()
        config_size_strings.append(trees_size_max_input)
        nflyers_min_input = self.nflyers_min.get()
        config_number_strings.append(nflyers_min_input)
        nflyers_max_input = self.nflyers_max.get()
        config_number_strings.append(nflyers_max_input)
        flyers_size_min_input = self.flyers_size_min.get()
        config_size_strings.append(flyers_size_min_input)
        flyers_size_max_input = self.flyers_size_max.get()
        config_size_strings.append(flyers_size_max_input)

        for i in config_number_strings:
            result = number_or_none(i)
            if result is None:
                return
            if result < 3:
                tkbox.showerror("Bad Value", "The input number is too small")
            if result > 20:
                tkbox.showerror("Bad Value", "The input number is too large")
            else:
                #  Store the result for later use
                config_numbers.append(result)

        for i in config_size_strings:
            result = float_or_none(i)
            if result is None:
                return
            if result < 0.3:
                tkbox.showerror("Bad Value", "The input size is too small")
            if result > 2.0:
                tkbox.showerror("Bad Value", "The input size is too large")
            else:
                config_sizes.append(result)

        global config
        config = forestconfig.ForestConfig(config_numbers[0],
                                           config_numbers[1], config_sizes[0],
                                           config_sizes[1], config_numbers[2],
                                           config_numbers[3], config_sizes[2],
                                           config_sizes[3], config_numbers[4],
                                           config_numbers[5], config_sizes[4],
                                           config_sizes[5])

        # Persist the config object into a file
        en = jsonpickle.encode(config, indent=2)
        with open("forestconfig.json", "w") as out_file:
            out_file.write(en)

        # close the tk window
        root.destroy()

    def run(self):
        """
        Run the forest simulation application.
        """
        root.mainloop()
        print("Ready to run the forest")


# MAIN PROGRAM
if __name__ == "__main__":

    def number_or_none(s):
        """Takes a string s and check if it could be converted to an integer.
        If not, pops up an error message"""
        try:
            return int(s)
        except ValueError:
            tkbox.showerror("Bad Value", "Argument is not a number")
            return None

    def float_or_none(s):
        """Takes a string s and check if it could be converted to a float.
        If not, pops up an error message"""
        try:
            return float(s)
        except ValueError:
            tkbox.showerror("Bad Value", "Argument is not a number")
            return None

    app = App()
    app.run()
