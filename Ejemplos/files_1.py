# Ejemplo detallado de File Handling en Python con comprobación y borrado
# -------------------------------------------------------------------
# Muestra: crear/sobrescribir, leer (completo y por líneas), añadir (append),
# comprobar existencia y borrar (con manejo de excepciones).
#
# Notas:
# - Usamos 'with open(...) as f:' para asegurar cierre automático del archivo.
# - Evitamos usar un if previo + remove (chequeo-then-act) sin manejar excepciones,
#   porque puede producir una race condition; por eso intentamos eliminar dentro de try/except.
# -------------------------------------------------------------------

import os
from pathlib import Path

# Nombre del archivo (puedes cambiarlo por una ruta absoluta si lo deseas)
filename = "mi_archivo.txt"

try:
    # -----------------------
    # 1) CREAR o SOBRESCRIBIR (modo "w")
    # -----------------------
    # Modo "w": si el archivo no existe, se crea; si existe, se TRUNCA (se borra su contenido).
    # Es buena práctica especificar encoding para tratar correctamente caracteres especiales.
    with open(filename, "w", encoding="utf-8") as f:
        # .write() escribe exactamente la cadena dada; añadir '\n' para saltos de línea.
        f.write("Hola, este es mi primer archivo en Python.\n")
        f.write("Estamos aprendiendo File Handling.\n")
    # Al salir del bloque with, el archivo se cierra automáticamente.
    print("Archivo creado y texto escrito correctamente.")

    # -----------------------
    # 2) LEER TODO EL CONTENIDO (modo "r")
    # -----------------------
    # Modo "r": abre en lectura; si no existe, lanza FileNotFoundError.
    with open(filename, "r", encoding="utf-8") as f:
        contenido = f.read()  # lee todo el contenido en una sola cadena
    print("\n--- Contenido del archivo (lectura completa) ---")
    print(contenido)

    # -----------------------
    # 3) AÑADIR CONTENIDO (modo "a" = append)
    # -----------------------
    # Modo "a": abre para añadir; si no existe, crea el archivo; si existe, no borra el contenido.
    with open(filename, "a", encoding="utf-8") as f:
        f.write("Esta línea fue añadida después.\n")
    print("\nNueva línea añadida correctamente.")

    # -----------------------
    # 4) LEER LÍNEA POR LÍNEA
    # -----------------------
    # Iterar sobre el objeto archivo es eficiente en memoria (ideal para archivos grandes).
    print("\n--- Lectura línea por línea ---")
    with open(filename, "r", encoding="utf-8") as f:
        for linea in f:
            # .rstrip("\n") elimina únicamente el '\n' final; .strip() quita espacios a ambos lados.
            print(linea.rstrip("\n"))

    # -----------------------
    # 5) COMPROBAR SI EL ARCHIVO EXISTE (os.path.exists)
    # -----------------------
    # os.path.exists devuelve True si la ruta existe (archivo o directorio).
    if os.path.exists(filename):
        print(f"\nEl archivo '{filename}' existe.")
    else:
        print(f"\nEl archivo '{filename}' NO existe.")

    # -----------------------
    # 6) BORRAR EL ARCHIVO (recomendado: intentar y capturar excepciones)
    # -----------------------
    # En lugar de: if exists -> remove (chequeo-then-act),
    # es mejor intentar os.remove e interceptar FileNotFoundError,
    # porque entre la comprobación y la eliminación otro proceso podría haber borrado el archivo.
    try:
        os.remove(filename)  # os.remove == os.unlink
        print(f"El archivo '{filename}' ha sido eliminado correctamente (os.remove).")
    except FileNotFoundError:
        # Si otro proceso borró el archivo antes de llamara os.remove
        print(f"No se puede borrar '{filename}': no existe (ya fue eliminado).")
    except PermissionError:
        # Si el script no tiene permisos para borrar el archivo
        print(f"No se pudo borrar '{filename}': permiso denegado.")
    except OSError as e:
        # Captura errores de sistema de archivos (p.ej. si filename es un directorio)
        print(f"Error al borrar '{filename}': {e}")

    # -----------------------
    # 7) ALTERNATIVA MODERNA: pathlib.Path
    # -----------------------
    # Path proporciona una API orientada a objetos para rutas de archivos.
    # Aquí demostramos cómo comprobar existencia y eliminar con Path.
    p = Path(filename)
    if p.exists():
        try:
            p.unlink()  # unlink() elimina el archivo; igual que os.remove
            print(f"(pathlib) Archivo '{filename}' eliminado usando Path.unlink().")
        except FileNotFoundError:
            print(f"(pathlib) El archivo '{filename}' no existe al intentar eliminarlo.")
        except PermissionError:
            print(f"(pathlib) No tienes permiso para borrar '{filename}'.")
        except Exception as e:
            print(f"(pathlib) Error al eliminar '{filename}': {e}")
    else:
        print(f"(pathlib) '{filename}' no existe (o ya fue eliminado).")

# -----------------------
# Manejo general de excepciones (seguro para operaciones de apertura/lectura/escritura)
# -----------------------
except FileNotFoundError as fnf:
    # Por ejemplo, si intentamos abrir en modo "r" y el archivo no existe.
    print("Error: archivo no encontrado:", fnf)
except PermissionError as pe:
    # Problemas de permisos (lectura/escritura/borrado)
    print("Error: permiso denegado:", pe)
except Exception as e:
    # Captura cualquier otra excepción inesperada y muestra información para depuración
    print("Ocurrió un error inesperado:", e)

"""
# --- FIN DEL EJEMPLO DE FILE HANDLING EN PYTHON ---
"""

"""
# NOTAS ADICIONALES:

Consejos y observaciones finales (resumen rápido)

Usa with open(...) para asegurar que el archivo se cierre aunque ocurra un error.

Maneja excepciones en las operaciones de borrado y apertura; evitar el patrón if exists: remove() sin capturar excepciones.

os.remove / Path.unlink() eliminan archivos; para directorios vacíos usa os.rmdir() o Path.rmdir().

Para archivos temporales usa el módulo tempfile (gestiona creación y borrado seguros).

Comprueba permisos si obtienes PermissionError.

pathlib es más moderno y expresivo; os es muy compatible y universal.
"""