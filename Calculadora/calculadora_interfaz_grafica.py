import tkinter as tk
from tkinter import messagebox
from sympy import sympify, sin, cos, tan, log
import math

# Historial de operaciones
history = []

# Funciones
def add_to_expression(symbol):
    expression = str(txt_expression.get())
    txt_expression.delete(0, tk.END)
    txt_expression.insert(0, expression + symbol)

def calculate(event=None):  # Añade event=None para que esta función se pueda ligar al evento de presionar "Enter"
    try:
        expression = str(txt_expression.get())
        result = sympify(expression).evalf()
        txt_result.delete(0, tk.END)
        txt_result.insert(0, str(result))
        history.append(f"{expression} = {result}")
    except Exception as e:
        messagebox.showerror("Error", "Operación inválida")

def clear():
    txt_expression.delete(0, tk.END)
    txt_result.delete(0, tk.END)

def square():
    try:
        expression = str(txt_expression.get())
        result = math.pow(sympify(expression).evalf(), 2)
        txt_result.delete(0, tk.END)
        txt_result.insert(0, str(result))
        history.append(f"{expression}² = {result}")
    except Exception as e:
        messagebox.showerror("Error", "Operación inválida")

def sqrt():
    try:
        expression = str(txt_expression.get())
        result = math.sqrt(sympify(expression).evalf())
        txt_result.delete(0, tk.END)
        txt_result.insert(0, str(result))
        history.append(f"√{expression} = {result}")
    except Exception as e:
        messagebox.showerror("Error", "Operación inválida")

def show_history():
    messagebox.showinfo("Historial", '\n'.join(history))

def clear_history():
    global history
    history = []
    messagebox.showinfo("Información", "Historial limpiado")

# GUI
window = tk.Tk()
window.geometry("300x600")
window.title("Calculadora Científica")

txt_expression = tk.Entry(window, width=40)
txt_expression.grid(row=0, column=0, columnspan=4)
txt_expression.bind('<Return>', calculate)  # Liga el evento de presionar "Enter" a la función calculate()

txt_result = tk.Entry(window, width=40)
txt_result.grid(row=1, column=0, columnspan=4)

# Aquí he añadido botones para funciones adicionales: sin, cos, tan y log
btn_sin = tk.Button(window, text="sin", command=lambda: add_to_expression('sin('), width=9, height=2)
btn_sin.grid(row=2, column=0)

btn_cos = tk.Button(window, text="cos", command=lambda: add_to_expression('cos('), width=9, height=2)
btn_cos.grid(row=2, column=1)

btn_tan = tk.Button(window, text="tan", command=lambda: add_to_expression('tan('), width=9, height=2)
btn_tan.grid(row=2, column=2)

btn_log = tk.Button(window, text="log", command=lambda: add_to_expression('log('), width=9, height=2)
btn_log.grid(row=2, column=3)

btn_calculate = tk.Button(window, text="Enter", command=calculate, width=9, height=2)
btn_calculate.grid(row=3, column=0)

btn_clear = tk.Button(window, text="Clear", command=clear, width=9, height=2)
btn_clear.grid(row=3, column=1)

btn_square = tk.Button(window, text="Square", command=square, width=9, height=2)
btn_square.grid(row=3, column=2)

btn_sqrt = tk.Button(window, text="Square Root", command=sqrt, width=9, height=2)
btn_sqrt.grid(row=3, column=3)

btn_history = tk.Button(window, text="Historial", command=show_history, width=9, height=2)
btn_history.grid(row=4, column=0)

btn_clear_history = tk.Button(window, text="Limpiar Historial", command=clear_history, width=9, height=2)
btn_clear_history.grid(row=4, column=1)

btns = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+'
]

row_val = 5
col_val = 0
for btn in btns:
    button = tk.Button(window, text=btn, width=9, height=2, command=lambda btn=btn: add_to_expression(btn))
    button.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
