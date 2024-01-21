import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self):
        self.app = tk.Tk()
        self.app.geometry("1500x750")
        self.app.title("SQL Chatbot")
        self.header = tk.Label(self.app, text="SQL Chatbot for GeoQuery Database", font = ("Helvetica", 40))
        self.header.pack(pady = 10)
        tk.Label(self.app, text="Enter the question you would like to ask:", font=("Helvetica", 20)).place(x = 40, y = 200)
        self.textInput = tk.Text(self.app, height = 1, width = 90, font = ("Helvetica", 20), fg = "#0f63d1")
        self.textInput.place(x=40, y=250)
        tk.Label(self.app, text="SQL Query:", font=("Helvetica", 20)).place(x = 40, y = 300)
        self.textOutputQuery = tk.Text(self.app, height = 2, width = 90, font = ("Helvetica", 20), fg = "#34b816")
        self.textOutputQuery.place(x=40, y=350)
        self.textOutputQuery.config(state=tk.DISABLED)
        tk.Label(self.app, text="Result:", font=("Helvetica", 20)).place(x = 40, y = 450)
        self.textOutputAnswer = tk.Text(self.app, height = 1, width = 90, font = ("Helvetica", 20), fg = "#34b816")
        self.textOutputAnswer.place(x=40, y=500)
        self.textOutputAnswer.config(state=tk.DISABLED)        

        self.app.mainloop()
