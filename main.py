import tkinter as tk
from tkinter import messagebox

# Допоміжні функції для обчислень
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

# Функції для роботи з інтерфейсом
def add():
    try:
        result = add_numbers(float(entry1.get()), float(entry2.get()))
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def subtract():
    try:
        result = subtract_numbers(float(entry1.get()), float(entry2.get()))
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def multiply():
    try:
        result = multiply_numbers(float(entry1.get()), float(entry2.get()))
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def divide():
    try:
        denominator = float(entry2.get())
        if denominator == 0:
            messagebox.showerror("Error", "Division by zero is not allowed")
        else:
            result = divide_numbers(float(entry1.get()), denominator)
            result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Створення інтерфейсу
window = tk.Tk()
window.title("Calculator")

# Поля вводу та кнопки
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

label1 = tk.Label(window, text="Enter first number:")
label1.grid(row=0, column=0)
label2 = tk.Label(window, text="Enter second number:")
label2.grid(row=1, column=0)

add_button = tk.Button(window, text="Додавання", command=add)
add_button.grid(row=2, column=0)
subtract_button = tk.Button(window, text="Subtract", command=subtract)
subtract_button.grid(row=2, column=1)
multiply_button = tk.Button(window, text="Multiply", command=multiply)
multiply_button.grid(row=3, column=0)
divide_button = tk.Button(window, text="Divide", command=divide)
divide_button.grid(row=3, column=1)

result_label = tk.Label(window, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

# Запуск вікна
'''
window.mainloop()
'''