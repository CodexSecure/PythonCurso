# --- Intentamos importar la librería Pillow (PIL) para manejar imágenes ---
try:
    from PIL import Image  # Pillow permite abrir y manipular imágenes (JPEG, PNG, etc.)
except ModuleNotFoundError:
    # Si no está instalada, mostramos un mensaje explicativo al usuario
    print("Error: Pillow no está instalado. Instálalo ejecutando:")
    print("    pip install Pillow")
    
    # Salimos del programa para evitar errores posteriores
    import sys
    sys.exit(1)

# --- Importamos las librerías necesarias ---

# gcd (Greatest Common Divisor): sirve para simplificar proporciones como 1920x1080 → 16:9
from math import gcd

# BytesIO nos permite tratar los datos descargados (bytes) como si fueran un archivo
from io import BytesIO

# requests permite descargar contenido desde una URL (en este caso, la imagen)
import requests


# --- Definición de la función principal ---
def calcular_aspect_ratio_url(url):
    """
    Descarga una imagen desde una URL y calcula su relación de aspecto (aspect ratio).

    Parámetro:
      - url: dirección web de la imagen (string)

    Retorna una tupla con:
      - ratio: cadena "ancho:alto" (por ejemplo, "16:9")
      - dimensiones: tupla (ancho, alto) en píxeles
      - orientación: texto "horizontal", "vertical" o "cuadrada"
    """

    # --- Paso 1: Descargar la imagen desde internet ---
    try:
        respuesta = requests.get(url)          # Descargamos el contenido desde la URL
        respuesta.raise_for_status()           # Lanza error si la descarga falla (404, 403, etc.)
    except requests.RequestException as e:
        print(f"No se pudo descargar la imagen: {e}")  # Mostramos el error
        return None  # Si falla la descarga, salimos de la función

    # --- Paso 2: Abrir la imagen y obtener su tamaño ---
    try:
        # Abrimos la imagen directamente desde la memoria sin guardarla en disco
        with Image.open(BytesIO(respuesta.content)) as img:
            ancho, alto = img.size  # Obtenemos las dimensiones de la imagen (width, height)

            # --- Paso 3: Calcular el aspect ratio simplificado ---
            divisor = gcd(ancho, alto)  # Calculamos el máximo común divisor
            ratio = f"{ancho // divisor}:{alto // divisor}"  # Simplificamos (ej: 1920x1080 → 16:9)

            # --- Paso 4: Determinar la orientación de la imagen ---
            if ancho > alto:
                orientacion = "horizontal"
            elif alto > ancho:
                orientacion = "vertical"
            else:
                orientacion = "cuadrada"

            # --- Paso 5: Devolver los resultados ---
            return ratio, (ancho, alto), orientacion

    except Exception as e:
        print(f"No se pudo abrir la imagen: {e}")  # Error si el archivo no es una imagen válida
        return None


# --- Ejemplo de uso ---
url = input("Introduce la URL de la imagen: ").strip()  # Pedimos al usuario la URL
resultado = calcular_aspect_ratio_url(url)  # Llamamos a la función

# --- Mostrar resultados ---
if resultado:
    ratio, (ancho, alto), orientacion = resultado
    print(f"Dimensiones: {ancho}x{alto}")      # Ej: "1920x1080"
    print(f"Aspect ratio: {ratio}")            # Ej: "16:9"
    print(f"Orientación: {orientacion}")       # Ej: "horizontal"
