import tkinter as tk
from tkinter import messagebox

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        return ""

def on_button_click(event):
    current_text = entry.get()
    new_text = current_text + event.widget.cget("text")
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def on_clear_click():
    entry.delete(0, tk.END)

def on_equal_click():
    expression = entry.get()
    result = evaluate_expression(expression)
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20)
    button.grid(row=row_val, column=col_val)
    if button_text == "=":
        button.bind("<Button-1>", lambda event: on_equal_click())
    else:
        button.bind("<Button-1>", on_button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

clear_button = tk.Button(root, text="C", padx=20, pady=20, command=on_clear_click)
clear_button.grid(row=row_val, column=col_val)

root.mainloop()