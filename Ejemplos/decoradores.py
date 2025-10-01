import time   # Importamos la librería time para medir tiempos de ejecución

# ================================
# 1) Decorador para medir tiempo
# ================================
def medir_tiempo(func):
    # Esta función envuelve a otra y calcula cuánto tarda en ejecutarse
    def wrapper(*args, **kwargs):
        inicio = time.time()   # Guardamos el tiempo inicial
        resultado = func(*args, **kwargs)  # Ejecutamos la función real
        fin = time.time()      # Guardamos el tiempo final
        print(f"⏱ Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado       # Devolvemos el resultado original
    return wrapper


# ================================
# 2) Decorador para permisos
# ================================
def requiere_admin(func):
    # Este decorador comprueba si el usuario es "admin"
    def wrapper(usuario, *args, **kwargs):
        if usuario != "admin":   # Si no es admin → no se ejecuta
            print("❌ Acceso denegado. Se requieren permisos de administrador.")
            return
        return func(usuario, *args, **kwargs)  # Si es admin → ejecutamos la función
    return wrapper


# ================================
# 3) Decorador para logging
# ================================
def log_funcion(func):
    # Este decorador imprime información antes y después de ejecutar la función
    def wrapper(*args, **kwargs):
        print(f"📋 Ejecutando {func.__name__} con args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)  # Ejecutamos la función
        print(f"✅ {func.__name__} terminó con resultado={resultado}")
        return resultado
    return wrapper


# ================================
# 4) Usando varios decoradores
# ================================
@medir_tiempo      # Mide el tiempo de ejecución (último en aplicarse)
@log_funcion       # Registra los argumentos y el resultado
@requiere_admin    # Comprueba si el usuario tiene permisos (se ejecuta primero)
def multiplicar(usuario, a, b):
    """Función que multiplica dos números"""
    return a * b   # Devuelve el producto de a y b


# ================================
# PRUEBAS
# ================================
print("\n--- Caso 1: usuario sin permisos ---")
multiplicar("juan", 4, 5)  # Como "juan" no es admin, no podrá ejecutar

print("\n--- Caso 2: usuario admin ---")
multiplicar("admin", 4, 5)  # Como es admin, sí se ejecuta toda la cadena de decoradores
