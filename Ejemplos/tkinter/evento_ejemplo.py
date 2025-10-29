from tkinter import *  # Importa todo el módulo Tkinter

root = Tk()  # Crea la ventana principal
root.title("Curso Tkinter")  # Título de la ventana
root.geometry("400x200")  # Tamaño de la ventana

"""
# ejemplo 1
def crear_etiqueta(numero_boton):
    etiqueta = Label(root, text=f"Boton {numero_boton} pulsado.")
    etiqueta.pack()

# Botones
boton_1 = Button(root, text="Boton 1", command=lambda:crear_etiqueta(1)).pack()
boton_2 = Button(root, text="Boton 2", command=lambda:crear_etiqueta(2)).pack()
boton_3 = Button(root, text="Boton 3", command=lambda:crear_etiqueta(3)).pack()
boton_4 = Button(root, text="Boton 4", command=lambda:crear_etiqueta(4)).pack()

"""
# ejemplo 2

# Nombre
Label(root, text="Nombre: ").grid(column=0, row=0)
entrada_nombre = Entry(root)
entrada_nombre.grid(column=1, row=0)

# Edad
Label(root, text="Edad: ").grid(column=0, row=1)
entrada_edad = Entry(root)
entrada_edad.grid(column=1, row=1)

# Evento para el boton
def pulsar_boton():
    # Se obtiene los valores de los Entry
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    # Se muetra en una etiqueta
    Label(root, text=f"Mi nombre es {nombre}. Tengo {edad} años.").grid(column=0, row=3, columnspan=4)

# Boton
Button(root, text="Enviar", command=pulsar_boton).grid(column=2, row=0, padx=5, rowspan=2)


root.mainloop()  # Inicia el bucle principal de la interfaz


