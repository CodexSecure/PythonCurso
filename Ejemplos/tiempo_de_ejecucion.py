import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱ Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def tarea_pesada():
    time.sleep(2)  # simula un proceso lento
    print("Tarea completada")

tarea_pesada()
