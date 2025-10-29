from tkinter import *  # Importa todo el módulo Tkinter

root = Tk()  # Crea la ventana principal
root.title("Curso Tkinter")  # Título de la ventana
root.geometry("400x200")  # Tamaño de la ventana

# Campo de texto (entrada)
entrada = Entry(root)
entrada.insert(0, "Escriba su nombre...")  # Texto inicial en la caja
entrada.bind("<Button-1>", lambda x: entrada.delete(0, END))  # Borra el texto al hacer clic izq
entrada.grid(row=0, column=0, padx=10, pady=10)  # Coloca el campo en la primera celda (fila 0, columna 0)

# Función que se ejecuta al pulsar el botón
def texto():
    nombre = entrada.get()  # Obtiene el texto escrito
    Label(root, text=nombre).grid(row=0, column=2, padx=5)  # Muestra el texto a la derecha

# Botón que llama a la función texto()
Button(root, text="Enviar!", command=texto).grid(row=0, column=1, padx=5)

root.mainloop()  # Inicia el bucle principal de la interfaz


