from tkinter import *
from math import sqrt

# Objeto ventana
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("400x600")  # Cambiado para un tamaño fijo para simplificar

# Frame para los botones
frame = Frame(ventana)
frame.pack(pady=20)

# Entrada para los números y resultados
entry = Entry(ventana, font=("Arial", 24), width=15, borderwidth=5)
entry.pack(pady=10)

# Función para actualizar la entrada con el número presionado
def click_button(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

# Función para limpiar la entrada
def clear():
    entry.delete(0, END)

# Función para la suma
def add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, END)

# Función para la resta
def subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)

# Función para la multiplicación
def multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)

# Función para la división
def divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, END)

# Función para el módulo
def mod():
    first_number = entry.get()
    global f_num
    global math
    math = "modulo"
    f_num = int(first_number)
    entry.delete(0, END)

# Función para la raíz cuadrada
def square_root():
    first_number = entry.get()
    entry.delete(0, END)
    entry.insert(0, sqrt(int(first_number)))

# Función para igual (realiza la operación)
def equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        entry.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        entry.insert(0, f_num * float(second_number))
    elif math == "division":
        entry.insert(0, f_num / float(second_number))
    elif math == "modulo":
        entry.insert(0, f_num % float(second_number))
    elif math == "square_root":
        # Para la raíz cuadrada, no necesitas un segundo número
        entry.insert(0, sqrt(f_num))

# Botón de limpiar
button_clear = Button(frame, text="Clear", padx=79, pady=20, command=clear)
# Organizar botón de limpiar en el frame
button_clear.grid(row=4, column=1, columnspan=2)

# Botones de números y operaciones
button_0 = Button(frame, text="0", padx=40, pady=20, command=lambda: click_button(0))
button_1 = Button(frame, text="1", padx=40, pady=20, command=lambda: click_button(1))
button_2 = Button(frame, text="2", padx=40, pady=20, command=lambda: click_button(2))
button_3 = Button(frame, text="3", padx=40, pady=20, command=lambda: click_button(3))
button_4 = Button(frame, text="4", padx=40, pady=20, command=lambda: click_button(4))
button_5 = Button(frame, text="5", padx=40, pady=20, command=lambda: click_button(5))
button_6 = Button(frame, text="6", padx=40, pady=20, command=lambda: click_button(6))
button_7 = Button(frame, text="7", padx=40, pady=20, command=lambda: click_button(7))
button_8 = Button(frame, text="8", padx=40, pady=20, command=lambda: click_button(8))
button_9 = Button(frame, text="9", padx=40, pady=20, command=lambda: click_button(9))
button_add = Button(frame, text="+", padx=39, pady=20, command=add)
button_subtract = Button(frame, text="-", padx=41, pady=20, command=subtract)
button_multiply = Button(frame, text="*", padx=40, pady=20, command=multiply)
button_divide = Button(frame, text="/", padx=40, pady=20, command=divide)
button_mod = Button(frame, text="%", padx=38, pady=20, command=mod)
button_sqrt = Button(frame, text="√", padx=38, pady=20, command=square_root)
button_equal = Button(frame, text="=", padx=91, pady=20, command=equal)

# Organizar botones en el frame
button_0.grid(row=4, column=0)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_mod.grid(row=7, column=0)
button_sqrt.grid(row=7, column=1)

# Cambiar todas las instancias de int() a float() en las funciones de operación
def add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, END)

def subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry.delete(0, END)

def multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, END)

def divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry.delete(0, END)

def mod():
    first_number = entry.get()
    global f_num
    global math
    math = "modulo"
    f_num = float(first_number)
    entry.delete(0, END)

# Actualizar la función square_root para establecer el valor global correcto
def square_root():
    first_number = entry.get()
    global f_num
    global math
    math = "square_root"
    f_num = float(first_number)
    entry.delete(0, END)
    entry.insert(0, sqrt(f_num))

ventana.mainloop()