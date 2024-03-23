import tkinter as tk

def print_text():
    text = entry.get()
    print(text)

# Create the main window
window = tk.Tk()
window.title("Print Text UI")

# Create an entry widget
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# Create a button to trigger the print function
print_button = tk.Button(window, text="Print Text", command=print_text)
print_button.pack()

# Run the tkinter event loop
window.mainloop()
