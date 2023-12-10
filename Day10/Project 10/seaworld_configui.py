"""CS 5001 - Kaiqi Zhang - Project 10 'Into the Sea World' - Configui file
"""

import seaworldconfig
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkbox
import jsonpickle


# instantiate global variables
root = tk.Tk()
global config
global checker


class App:
    """
    Represents the main application for running the seawolrd simulation.

    """

    def __init__(self):
        """
        Initialize the App object.
        """
        root.title("Into The Sea World")
        my_frame = ttk.Frame(root, padding=10)
        my_frame.grid()
        ttk.Label(my_frame, text="Minimum number of fishes in each fish group:"
                  ).grid(
            row=0, column=0)
        ttk.Label(my_frame, text="Maximum number of fishes in each fish group:"
                  ).grid(
            row=1, column=0)
        ttk.Label(my_frame, text="Minimum size of fish:").grid(
            row=2, column=0)
        ttk.Label(my_frame, text="Maximum size of fish:").grid(
            row=3, column=0)
        ttk.Label(my_frame, text="Minimum number of seastars:").grid(
            row=4, column=0)
        ttk.Label(my_frame, text="Maximum numbers of seastars:").grid(
            row=5, column=0)
        ttk.Label(my_frame, text="Minimum size of seastars:").grid(
            row=6, column=0)
        ttk.Label(my_frame, text="Maximum size of seastars:").grid(
            row=7, column=0)
        ttk.Label(my_frame, text="Minimum number of clusters of seagrass:"
                  ).grid(
            row=8, column=0)
        ttk.Label(my_frame, text="Maximum number of clusters of seagrass:"
                  ).grid(
            row=9, column=0)
        ttk.Label(my_frame, text="Minimum size of seagrass clusters:").grid(
            row=10, column=0)
        ttk.Label(my_frame, text="Maximum size of seagrass clusters:").grid(
            row=11, column=0)

        ttk.Button(my_frame, text="Save",
                   command=self.on_start).grid(row=12, column=0)

        self.nfish_min = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.nfish_min).grid(row=0, column=1)
        self.nfish_max = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.nfish_max).grid(row=1, column=1)
        self.fish_size_min = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.fish_size_min).grid(row=2,
                                                                  column=1)
        self.fish_size_max = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.fish_size_max).grid(row=3,
                                                                  column=1)
        self.nseastar_min = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.nseastar_min).grid(row=4,
                                                                 column=1)
        self.nseastar_max = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.nseastar_max).grid(row=5,
                                                                 column=1)
        self.seastar_size_min = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.seastar_size_min).grid(row=6,
                                                                     column=1)
        self.seastar_size_max = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.seastar_size_max).grid(row=7,
                                                                     column=1)
        self.nseagrassCluster_min = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.nseagrassCluster_min).grid(
            row=8, column=1)
        self.nseagrassCluster_max = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.nseagrassCluster_max).grid(
            row=9, column=1)
        self.seagrassCluster_size_min = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.seagrassCluster_size_min).grid(
            row=10, column=1)
        self.seagrassCluster_size_max = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.seagrassCluster_size_max).grid(
            row=11, column=1)

    def on_start(self):
        """Convert user input into strings, validate input values,
        and set up the configuration using these values."""
        config_number_strings = []
        config_size_strings = []
        config_numbers = []
        config_sizes = []

        # get string value out of each StringVar object
        nfish_min_input = self.nfish_min.get()
        config_number_strings.append(nfish_min_input)
        nfish_max_input = self.nfish_max.get()
        config_number_strings.append(nfish_max_input)
        fish_size_min_input = self.fish_size_min.get()
        config_size_strings.append(fish_size_min_input)
        fish_size_max_input = self.fish_size_max.get()
        config_size_strings.append(fish_size_max_input)

        nseastar_min_input = self.nseastar_min.get()
        config_number_strings.append(nseastar_min_input)
        nseastar_max_input = self.nseastar_max.get()
        config_number_strings.append(nseastar_max_input)
        seastar_size_min_input = self.seastar_size_min.get()
        config_size_strings.append(seastar_size_min_input)
        seastar_size_max_input = self.seastar_size_max.get()
        config_size_strings.append(seastar_size_max_input)

        nseagrassCluster_min_input = self.nseagrassCluster_min.get()
        config_number_strings.append(nseagrassCluster_min_input)
        nseagrassCluster_max_input = self.nseagrassCluster_max.get()
        config_number_strings.append(nseagrassCluster_max_input)
        seagrassCluster_size_min_input = self.seagrassCluster_size_min.get()
        config_size_strings.append(seagrassCluster_size_min_input)
        seagrassCluster_size_max_input = self.seagrassCluster_size_max.get()
        config_size_strings.append(seagrassCluster_size_max_input)

        checker = InputCheck()
        for i in config_number_strings:
            result = checker.number_or_none(i)
            if result is None:
                return
            if result < 2:
                tkbox.showerror("Bad Value! The input number is too small. \
                                Please input a value that is greater than 2")
            if result > 20:
                tkbox.showerror("Bad Value! The input number is too large.\
                                Please input a value that is less than 20")
            else:
                #  Store the result for later use
                config_numbers.append(result)

        for i in config_size_strings:
            result = checker.float_or_none(i)
            if result is None:
                return
            if result < 0.3:
                tkbox.showerror("Bad Value! The input size is too small.\
                                Please input a value that is greater than 0.3")
            if result > 2.0:
                tkbox.showerror("Bad Value! The input size is too large.\
                                Please input a value that is less than 2.0")
            else:
                config_sizes.append(result)

        global config
        config = seaworldconfig.SeaworldConfig(config_numbers[0],
                                               config_numbers[1],
                                               config_sizes[0],
                                               config_sizes[1],
                                               config_numbers[2],
                                               config_numbers[3],
                                               config_sizes[2],
                                               config_sizes[3],
                                               config_numbers[4],
                                               config_numbers[5],
                                               config_sizes[4],
                                               config_sizes[5])

        # Persist the config object into a file
        en = jsonpickle.encode(config, indent=2)
        with open("seaworldconfig.json", "w") as out_file:
            out_file.write(en)

        # close the tk window
        root.destroy()

    def run(self):
        """
        Run the seaworld simulation application.
        """
        root.mainloop()
        print("Ready to run Into the Seaworld")


class InputCheck:
    def __init__(self) -> None:
        pass

    def number_or_none(self, s):
        """Takes a string s and check if it could be converted to an integer.
        If not, pops up an error message"""
        try:
            return int(s)
        except ValueError:
            tkbox.showerror("Bad Value", "Argument is not a number")
            return None

    def float_or_none(self, s):
        """Takes a string s and check if it could be converted to a float.
        If not, pops up an error message"""
        try:
            return float(s)
        except ValueError:
            tkbox.showerror("Bad Value", "Argument is not a number")
            return None


# MAIN PROGRAM
if __name__ == "__main__":

    app = App()
    app.run()
