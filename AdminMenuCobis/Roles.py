import tkinter as tk
from tkinter import ttk
import pandas as pd

class Role:
    def __init__(self, name):
        self.name = name
        self.menu_options = {}
    
    def add_menu_option(self, option):
        self.menu_options[option] = False  # Inicialmente no marcado
    
    def get_menu_options(self):
        return self.menu_options.keys()
    
    def set_option_state(self, option, state):
        if option in self.menu_options:
            self.menu_options[option] = state

def create_ui(roles):
    def update_option_state(role, option, var):
        role.set_option_state(option, var.get())
    
    root = tk.Tk()
    root.title("Roles y Opciones de Menú")
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Guardar", command=save_options)
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=root.quit)
    menubar.add_cascade(label="Archivo", menu=filemenu)
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Retroceso", command=undo_action)
    menubar.add_cascade(label="Edición", menu=editmenu)
    root.config(menu=menubar)

    for role in roles:
        frame = ttk.LabelFrame(root, text=role.name)
        frame.pack(padx=10, pady=5, fill='x', expand=True)
        for option in role.get_menu_options():
            var = tk.BooleanVar(value=False)
            chk = ttk.Checkbutton(frame, text=option, variable=var, 
                                  command=lambda option=option, var=var, role=role: update_option_state(role, option, var))
            chk.pack(side='top', anchor='w')
    
    export_button = ttk.Button(root, text="Exportar a xlsx", command=lambda: export_to_xlsx(roles))
    export_button.pack(pady=10)
    root.mainloop()

def export_to_xlsx(roles):
    print("Exportando roles a xlsx...")
    data = []
    for role in roles:
        for option, state in role.menu_options.items():
            data.append({"Role": role.name, "Option": option, "Checked": "Sí" if state else "No"})
    df = pd.DataFrame(data)
    df.to_excel("roles.xlsx", index=False)

def save_options():
    print("Opciones guardadas")

def undo_action():
    print("Acción de retroceso realizada")

# Crear roles y opciones de menú
subgerente = Role("SUBGERENTE")
opciones_menu = [
    "Clientes", "Operaciones", "Administración", "Informacion Cliente",
    "Revision de Listas de Control", "Malas Referencias",
    "Mantenimiento Situación Económica y Patrimonial", "Tipos de Identificación",
    "Mantenimiento Rol", "Tipo de Relaciones", "Datos Adicionales",
    "Actividades Economicas", "Segmentos", "Perfil de riesgo",
    "Parametrización Mascara de Teléfonos"
]

for option in opciones_menu:
    subgerente.add_menu_option(option)

# Crear y mostrar la UI
create_ui([subgerente])






