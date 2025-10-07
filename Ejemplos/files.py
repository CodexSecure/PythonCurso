# --- FILE HANDLING EN PYTHON ---
# Ejemplo completo: crear, escribir, leer, añadir contenido y manejar errores

try:
    # 1. Crear o sobrescribir un archivo en modo escritura ("w")
    # Si el archivo no existe, se crea. Si existe, borra lo que tenía.
    with open("mi_archivo.txt", "w") as f:
        f.write("Hola, este es mi primer archivo en Python.\n")   # primera línea
        f.write("Estamos aprendiendo File Handling.\n")          # segunda línea
    print("Archivo creado y texto escrito correctamente.")

    # 2. Abrir el archivo en modo lectura ("r")
    # Aquí leemos todo el contenido de golpe
    with open("mi_archivo.txt", "r") as f:
        contenido = f.read()   # almacena todo el texto en la variable contenido
    print("\n--- Contenido del archivo ---")
    print(contenido)  # mostramos lo que leímos

    # 3. Abrir el archivo en modo añadir ("a")
    # Esto no borra lo anterior, simplemente escribe al final
    with open("mi_archivo.txt", "a") as f:
        f.write("Esta línea fue añadida después.\n")  # línea nueva
    print("\nNueva línea añadida correctamente.")

    # 4. Leer línea por línea con un bucle
    # Ahora volvemos a abrir en modo lectura para ver todo línea por línea
    with open("mi_archivo.txt", "r") as f:
        print("\n--- Lectura línea por línea ---")
        for linea in f:
            print(linea.strip())  # .strip() quita saltos de línea al final

# 5. Manejo de errores
except FileNotFoundError:
    print("Error: El archivo no existe.")
except PermissionError:
    print("Error: No tienes permisos para acceder al archivo.")
except Exception as e:
    print("Ocurrió un error inesperado:", e)




