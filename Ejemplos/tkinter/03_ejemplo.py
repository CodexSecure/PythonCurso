import tkinter as tk
from tkinter import ttk
import platform
import psutil

# Función para obtener información del sistema
def obtener_info():
    info = {
        "Sistema": platform.system(),
        "Nombre de la PC": platform.node(),
        "Versión SO": platform.version(),
        "Release SO": platform.release(),
        "Arquitectura": platform.machine(),
        "Procesador": platform.processor(),
        "CPU cores": psutil.cpu_count(logical=False),
        "CPU threads": psutil.cpu_count(logical=True),
        "Memoria total": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB"
    }
    return info

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Propiedades del PC")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Etiqueta de título
titulo = tk.Label(ventana, text="Información de tu PC", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Frame para mostrar la info
frame = tk.Frame(ventana)
frame.pack(pady=10)

# Mostrar la información
info = obtener_info()
for clave, valor in info.items():
    fila = tk.Frame(frame)
    fila.pack(anchor="w", pady=2)

    tk.Label(fila, text=f"{clave}:", font=("Arial", 12, "bold")).pack(side="left")
    tk.Label(fila, text=f"{valor}", font=("Arial", 12)).pack(side="left")

# Botón para cerrar
btn_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
btn_cerrar.pack(pady=20)

# Ejecutar el loop principal
ventana.mainloop()
