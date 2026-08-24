import tkinter as tk
from tkinter import messagebox
def press_key(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

# Функция для очистки экрана (кнопка C)
def clear():
    entry.delete(0, tk.END)

# Функция для удаления последнего символа (кнопка Backspace)
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def calculate():
    try:
        expression = entry.get()
        expression = expression.replace('×', '*').replace('÷', '/')
        result = eval(expression)
        
        if isinstance(result, float) and result.is_integer():
            result = int(result)
            
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "Деление на ноль невозможно!")
        clear()
    except Exception:
        messagebox.showerror("Ошибка", "Неверное выражение!")
        clear()
root = tk.Tk()
root.title("Калькулятор")
root.geometry("320x450")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, insertwidth=4, width=14, borderwidth=0)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

buttons = [
    ('C', 1, 0), ('⌫', 1, 1), ('(', 1, 2), (')', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('÷', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('×', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3)
]
for (text, row, col) in buttons:
    f_font = ("Arial", 14)
    f_height = 2
    f_width = 5

    if text == '=':
        btn = tk.Button(root, text=text, font=f_font, height=f_height, width=f_width, borderwidth=0,
                        bg="#4CAF50", fg="white", activebackground="#45a049", command=calculate)
    elif text in ['C', '⌫']:
        action = clear if text == 'C' else backspace
        btn = tk.Button(root, text=text, font=f_font, height=f_height, width=f_width, borderwidth=0,
                        bg="#ff9800", fg="white", activebackground="#e68a00", command=action)
    elif text in ['+', '-', '×', '÷', '(', ')']:
        btn = tk.Button(root, text=text, font=f_font, height=f_height, width=f_width, borderwidth=0,
                        bg="#e0e0e0", fg="#000000", activebackground="#d9d9d9", command=lambda t=text: press_key(t))
    else:
        btn = tk.Button(root, text=text, font=f_font, height=f_height, width=f_width, borderwidth=0,
                        bg="#ffffff", fg="#000000", activebackground="#d9d9d9", command=lambda t=text: press_key(t))
        
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
root.mainloop()