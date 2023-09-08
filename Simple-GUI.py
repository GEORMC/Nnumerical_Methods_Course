import tkinter as tk

def calculate_sum():
    try:
        A = float(entry_a.get())
        B = float(entry_b.get())
        result.set(f"Result: {A + B}")
    except ValueError:
        result.set("Invalid input!")

# Create a tkinter window
window = tk.Tk()
window.title("Simple Summation Calculator")

# Create labels and entry fields for A and B
label_a = tk.Label(window, text="A:")
label_b = tk.Label(window, text="B:")
entry_a = tk.Entry(window)
entry_b = tk.Entry(window)

label_a.grid(row=0, column=0)
label_b.grid(row=1, column=0)
entry_a.grid(row=0, column=1)
entry_b.grid(row=1, column=1)

# Create a button to calculate the sum
calculate_button = tk.Button(window, text="Calculate Sum", command=calculate_sum)
calculate_button.grid(row=2, columnspan=2)

# Display the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.grid(row=3, columnspan=2)

# Start the GUI main loop
window.mainloop()
