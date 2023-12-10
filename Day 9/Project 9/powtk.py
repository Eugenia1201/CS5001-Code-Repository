""" CS 5001 - Day 9 - Lab 9 - "Graphical Pow" - Kaiqi Zhang - 15 Nov """

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkbox


class TooBigError(ValueError):
    pass


def pow(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    if a > 10 or b > 10:
        raise TooBigError
    else:
        return a ** b


def number_or_none(s):
    try:
        return float(s)
    except ValueError:
        tkbox.showerror("Bad Value", "Argument is not a number")
        return None


def on_pow():
    input_a = a_string.get()
    input_b = b_string.get()
    a = number_or_none(input_a)
    b = number_or_none(input_b)
    if (a is not None) and (b is not None):
        try:
            result = pow(a, b)
            tkbox.showinfo("Pow", f"Result is {result}")
        except TooBigError:
            tkbox.showerror("Too Big", "Argument must not be greater than 10")
        except ValueError:
            tkbox.showerror("Positive", "Argument must be positive")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pow!")
    my_frame = ttk.Frame(root, padding=10)
    my_frame.grid()
    ttk.Label(my_frame, text="A:").grid(row=0, column=0)
    ttk.Label(my_frame, text="B:").grid(row=1, column=0)
    a_string = tk.StringVar()
    ttk.Entry(my_frame, textvariable=a_string).grid(row=0, column=1)
    b_string = tk.StringVar()
    ttk.Entry(my_frame, textvariable=b_string).grid(row=1, column=1)
    ttk.Button(my_frame, text="POW", command=on_pow).grid(row=2, column=1)

    root.mainloop()
