def con_return(a, b):
    # Esta función devuelve el resultado para poder usarlo fuera
    calc = a + b
    return calc

def sin_return(a, b):
    # Esta función solo muestra el resultado, pero no devuelve nada
    print(a + b)  

# ==========================
# Ejemplo con return
# ==========================
resultadoA = con_return(2, 3)  
print("Resultado guardado (con return):", resultadoA)  # 5

# ==========================
# Ejemplo sin return
# ==========================
sin_return(2, 3)  # Imprime 5, pero no devuelve nada
resultadoB = sin_return(2, 3)  # Muestra 5, pero devuelve None
print("Resultado guardado (sin return):", resultadoB)  # None