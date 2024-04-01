
import tkinter as tk
from tkinter import messagebox

class App:

    def __init__(self, callback):
        self.app = tk.Tk()
        self.app.geometry("1500x750")
        self.app.title("SQL Chatbot")
        self.header = tk.Label(self.app, text="SQL Chatbot for GeoQuery Database", font = ("Helvetica", 40))
        self.header.pack(pady = 10)
        tk.Label(self.app, text="Enter the question you would like to ask:", font=("Helvetica", 20)).place(x = 40, y = 100)
        self.textInput = tk.Text(self.app, height = 1, width = 90, font = ("Helvetica", 20), fg = "#0f63d1")
        self.textInput.place(x=40, y=150)
        self.send_button = tk.Button(self.app, text="Generate answer", command = self.btn_send)
        self.send_button.place(x=150, y=200)
        tk.Label(self.app, text="Generated SQL Query:", font=("Helvetica", 20)).place(x = 40, y = 250)
        self.textOutputQuery = tk.Text(self.app, height = 2, width = 90, font = ("Helvetica", 20), fg = "#34b816")
        self.textOutputQuery.place(x=40, y=300)
        self.textOutputQuery.config(state=tk.DISABLED)
        tk.Label(self.app, text="Generated SQL Query Result:", font=("Helvetica", 20)).place(x = 40, y = 400)
        self.textOutputQueryExecute = tk.Text(self.app, height = 2, width = 90, font = ("Helvetica", 20), fg = "#34b816")
        self.textOutputQueryExecute.place(x=40, y=450)
        self.textOutputQueryExecute.config(state=tk.DISABLED)
        tk.Label(self.app, text="Generated Answer:", font=("Helvetica", 20)).place(x = 40, y = 550)
        self.textOutputAnswer = tk.Text(self.app, height = 3, width = 90, font = ("Helvetica", 20), fg = "#34b816")
        self.textOutputAnswer.place(x=40, y=600)
        self.textOutputAnswer.config(state=tk.DISABLED)        
        self.callback = callback
        self.clear_button = tk.Button(self.app, text="Clear", command = self.clear_textboxes)
        self.clear_button.place(x=250, y=200)
        self.textInput.bind("<Return>", self.btn_enter)
        self.textInput.bind("<Tab>", self.focus_next_widget)
        self.send_button.bind("<Return>", self.btn_enter)
        self.clear_button.bind("<Return>", self.tab_clear_textboxes)

    def btn_send(self):
        self.query = self.textInput.get("1.0",'end-1c')
        self.textOutputQuery.config(state=tk.NORMAL)
        self.textOutputQuery.delete(1.0, tk.END)
        self.textOutputQuery.config(state=tk.DISABLED)
        self.textOutputAnswer.config(state=tk.NORMAL)
        self.textOutputAnswer.delete(1.0, tk.END)
        self.textOutputAnswer.config(state=tk.DISABLED)
        self.textOutputQueryExecute.config(state=tk.NORMAL)
        self.textOutputQueryExecute.delete(1.0, tk.END)
        self.textOutputQueryExecute.config(state=tk.DISABLED)
        self.callback(self.query)

    def query_out(self, result):
        self.textOutputQuery.config(state=tk.NORMAL)
        self.textOutputQuery.insert(tk.END, result)
        self.textOutputQuery.config(state=tk.DISABLED)

    def query_execute_out(self, result):
        self.textOutputQueryExecute.config(state=tk.NORMAL)
        self.textOutputQueryExecute.insert(tk.END, result)
        self.textOutputQueryExecute.config(state=tk.DISABLED)

    def result_out(self, result):
        self.textOutputAnswer.config(state=tk.NORMAL)
        self.textOutputAnswer.insert(tk.END, result)
        self.textOutputAnswer.config(state=tk.DISABLED)

    def clear_textboxes(self):
        self.textInput.delete(1.0, tk.END)
        self.textOutputQuery.config(state=tk.NORMAL)
        self.textOutputQuery.delete(1.0, tk.END)
        self.textOutputQuery.config(state=tk.DISABLED)
        self.textOutputAnswer.config(state=tk.NORMAL)
        self.textOutputAnswer.delete(1.0, tk.END)
        self.textOutputAnswer.config(state=tk.DISABLED)
        self.textOutputQueryExecute.config(state=tk.NORMAL)
        self.textOutputQueryExecute.delete(1.0, tk.END)
        self.textOutputQueryExecute.config(state=tk.DISABLED)

    def btn_enter(self, event = None):
        self.send_button.invoke()
        return 'break'
    
    def focus_next_widget(self, event=None):
            event.widget.tk_focusNext().focus()
            return "break"

    def tab_clear_textboxes(self, event = None):
        self.textInput.delete(1.0, tk.END)
        self.textOutputQuery.config(state=tk.NORMAL)
        self.textOutputQuery.delete(1.0, tk.END)
        self.textOutputQuery.config(state=tk.DISABLED)
        self.textOutputAnswer.config(state=tk.NORMAL)
        self.textOutputAnswer.delete(1.0, tk.END)
        self.textOutputAnswer.config(state=tk.DISABLED)
        self.textOutputQueryExecute.config(state=tk.NORMAL)
        self.textOutputQueryExecute.delete(1.0, tk.END)
        self.textOutputQueryExecute.config(state=tk.DISABLED)
        return 'break'