import tkinter as tk

# Function to update the display when a button is pressed
def update_display(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

# Function to calculate the result
def calculate_result():
    try:
        result = eval(display.get())  # Evaluate the mathematical expression
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")  # Set window size

# Create the display area (an entry widget to show the input and output)
display = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
display.grid(row=0, column=0, columnspan=4)

# Define the buttons and their positions in the grid
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)  # The '=' button spans 4 columns
]

# Create and place buttons on the grid
for button in buttons:
    text, row, col = button[:3]
    if text == '=':
        btn = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=calculate_result)
        btn.grid(row=row, column=col, columnspan=4)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=clear_display)
        btn.grid(row=row, column=col)
    else:
        btn = tk.Button(root, text=text, width=5, height=3, font=("Arial", 18),
                        command=lambda t=text: update_display(t))
        btn.grid(row=row, column=col)

# Start the Tkinter event loop to run the calculator
root.mainloop()
