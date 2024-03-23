import tkinter as tk
from tkinter import messagebox

def validate_string():
    try:
        str_input = text_input.get()
        output_1.delete(1.0, tk.END)
        output_2.delete(1.0, tk.END)
        output_1.insert(tk.END, "Your string is: {}".format(str_input))
        output_2.insert(tk.END, "The length of your string is: {}".format(len(str_input)))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_all():
    text_input.delete(0, tk.END)
    output_1.delete(1.0, tk.END)
    output_2.delete(1.0, tk.END)

app = tk.Tk()
app.title("String Validator")

header = tk.Label(app, text="String Validator", font=("Arial", 20))
header.pack(pady=10)

text_input = tk.Entry(app, width=50)
text_input.pack(pady=10)

validate_button = tk.Button(app, text="Validate", command=validate_string)
validate_button.pack(pady=10)

clear_button = tk.Button(app, text="Clear All", command=clear_all)
clear_button.pack(pady=10)

output_1 = tk.Text(app, width=50, height=1)
output_1.pack(pady=10)

output_2 = tk.Text(app, width=50, height=1)
output_2.pack(pady=10)

app.mainloop()