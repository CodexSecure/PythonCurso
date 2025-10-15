import time
import math

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()   # Guardamos el tiempo inicial
        resultado = func(*args, **kwargs)  # Ejecutamos la función real
        fin = time.time()      # Guardamos el tiempo final
        print(f"Tiempo de ejecución: {fin - inicio:.10f} segundos")
        return resultado       # Devolvemos el resultado original
    return wrapper

@medir_tiempo
def myfunction(a,b):	
    c = math.hypot(a, b)
    if c > 5:
        hipo = "grande"        
    else:
        hipo = "pequeña"
    print(f"La hipotenusa es: {c} y es {hipo}")    

myfunction(4,9)