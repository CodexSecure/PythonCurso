from tkinter import *

root = Tk()

root.title("Mi primera GUI")
root.geometry("600x400+200+200")  # ancho x alto
"""
mensaje = Label(root, text="Mi primer progama con Tkinter.")
mensaje_2 = Label(root, text="Esta es la segunda etiqueta.")

mensaje.grid(row=1, column=0)
mensaje_2.grid(row=0, column=1)

"""
mensaje = Label(root, text="Mi primer progama con Tkinter.").grid(row=1, column=0)
mensaje_2 = Label(root, text="Esta es la segunda etiqueta.").grid(row=0, column=1)

# Crear un botón
def saludar():
    print("¡Hola desde el botón!")

boton = Button(root, text="Saludar", command=saludar)
boton.grid(row=2, column=2)

root.mainloop()