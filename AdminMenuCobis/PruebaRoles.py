import tkinter as tk


'''
MENU SUBGERENTE
    *CAJAS
        **ADMINISTRACIÓN DE CAJA
            ***Reglas y parámetros
                ****Supervisores
            ***Control bóveda y efectivo
                ****Mantenimiento de caja y límites específico
            ***Procesos
                ****Inicio de día
                ****Cierre de sucursal
        **CONSULTAS
            ***Monitor de caja
            ***Monitor de caja (histórico)
            ***Estados de cierre de sucursal
            ***Transacciones monetarias
            ***Transacciones monetarias (Supervisor)
            ***Transacciones monetarias (Tesorero)
            ***Reporte de reversos
            ***Tira auditora
            ***Tira auditora (supervisor)
        **TRANSACCIONES DE CAJA
            ***01 - apertura de caja
            ***26380 - otros ingresos bóveda
            ***26381 - otros egresos bóveda
            ***Transferencias de efectivo
            ***Transferencias pendientes
            ***Transacciones a reversar
            ***Totales y cuadres parciales
            ***Totales y cuadre  
'''
# Create the root window
root = tk.Tk()

# Create the main menu
main_menu = tk.Menu(root)
root.config(menu=main_menu)

# Create the "Cajas" submenu
cajas_submenu = tk.Menu(main_menu)
main_menu.add_cascade(label="Cajas", menu=cajas_submenu)

# Create the "Administración de Caja" submenu
admin_caja_submenu = tk.Menu(cajas_submenu)
cajas_submenu.add_cascade(label="Administración de Caja", menu=admin_caja_submenu)

# Create the "Reglas y parámetros" submenu
reglas_submenu = tk.Menu(admin_caja_submenu)
admin_caja_submenu.add_cascade(label="Reglas y parámetros", menu=reglas_submenu)

# Add items to the "Reglas y parámetros" submenu
reglas_submenu.add_command(label="Supervisores")

# Create the "Control bóveda y efectivo" submenu
control_submenu = tk.Menu(admin_caja_submenu)
admin_caja_submenu.add_cascade(label="Control bóveda y efectivo", menu=control_submenu)

# Add items to the "Control bóveda y efectivo" submenu
control_submenu.add_command(label="Mantenimiento de caja y límites específico")

# Create the "Procesos" submenu
procesos_submenu = tk.Menu(admin_caja_submenu)
admin_caja_submenu.add_cascade(label="Procesos", menu=procesos_submenu)

# Add items to the "Procesos" submenu
procesos_submenu.add_command(label="Inicio de día")
procesos_submenu.add_command(label="Cierre de sucursal")

# Create the "Consultas" submenu
consultas_submenu = tk.Menu(cajas_submenu)
cajas_submenu.add_cascade(label="Consultas", menu=consultas_submenu)

# Add items to the "Consultas" submenu
consultas_submenu.add_command(label="Monitor de caja")
consultas_submenu.add_command(label="Monitor de caja (histórico)")
consultas_submenu.add_command(label="Estados de cierre de sucursal")
consultas_submenu.add_command(label="Transacciones monetarias")
consultas_submenu.add_command(label="Transacciones monetarias (Supervisor)")
consultas_submenu.add_command(label="Transacciones monetarias (Tesorero)")
consultas_submenu.add_command(label="Reporte de reversos")
consultas_submenu.add_command(label="Tira auditora")
consultas_submenu.add_command(label="Tira auditora (supervisor)")

# Create the "Transacciones de Caja" submenu
transacciones_submenu = tk.Menu(cajas_submenu)
cajas_submenu.add_cascade(label="Transacciones de Caja", menu=transacciones_submenu)

# Add items to the "Transacciones de Caja" submenu
transacciones_submenu.add_command(label="01 - apertura de caja")
transacciones_submenu.add_command(label="26380 - otros ingresos bóveda")
transacciones_submenu.add_command(label="26381 - otros egresos bóveda")
transacciones_submenu.add_command(label="Transferencias de efectivo")
transacciones_submenu.add_command(label="Transferencias pendientes")
transacciones_submenu.add_command(label="Transacciones a reversar")
transacciones_submenu.add_command(label="Totales y cuadres parciales")
transacciones_submenu.add_command(label="Totales y cuadre")

# Run the main loop
root.mainloop()
