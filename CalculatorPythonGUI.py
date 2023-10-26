# Import the tkinter library for GUI
import tkinter as tk
from tkinter import messagebox

# Defines functions for arithmetic operations
def addition():
    try:
        # Gets the values from the input fields, convert to float, and sets the result
        result.set(float(val1.get()) + float(val2.get()))
    except ValueError:
        # Handles invalid input with a message box
        messagebox.showerror("Error", "Invalid input")

def subtraction():
    try:
        result.set(float(val1.get()) - float(val2.get()))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def multiply():
    try:
        result.set(float(val1.get()) * float(val2.get()))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def division():
    try:
        # Get the divisor and handle division by zero
        divisor = float(val2.get())
        if divisor == 0:
            raise ZeroDivisionError
        result.set(float(val1.get()) / divisor)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")

# Creates the main window
root = tk.Tk()
root.title("Simple GUI Calculator")  # Set the window title

# Creates input fields and labels
val1_label = tk.Label(root, text="Enter your 1st value:")  # Create a label
val1_label.pack()  # Pack the label into the window
val1 = tk.Entry(root)  # Create an input field
val1.pack()  # Pack the input field into the window

val2_label = tk.Label(root, text="Enter your 2nd value:")  # Create another label
val2_label.pack()  # Pack the label into the window
val2 = tk.Entry(root)  # Create another input field
val2.pack()  # Pack the input field into the window

# Creates buttons for each operation
#Makes a button for the operation, stores it in the root window,
#Has the word of the operation, and when pressed, it runs the command.

add_button = tk.Button(root, text="Add", command=addition)  # Create a button with a callback function
add_button.pack()  # Pack the button into the window

subtract_button = tk.Button(root, text="Subtract", command=subtraction) 
subtract_button.pack()

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.pack()

divide_button = tk.Button(root, text="Divide", command=division)
divide_button.pack()

# Create a variable to hold the result and a label to display it
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

# Run the GUI event loop
root.mainloop()

