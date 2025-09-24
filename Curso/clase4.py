# 📝 Ejercicio: Sumar dos artículos y aplicar IVA

# Pedimos los precios
articulo1 = float(input("Introduce el precio del primer artículo: "))
articulo2 = float(input("Introduce el precio del segundo artículo: "))

# Sumamos los dos precios
subtotal = articulo1 + articulo2

# Definimos el IVA (21%)
IVA = 0.21

# Calculamos el total con IVA
total_con_iva = subtotal * (1 + IVA)

# Mostramos resultados
if total_con_iva < 15:
    print("\n--- RESULTADO ---")
    print(f"Subtotal (sin IVA): {subtotal:.2f} €")
    print(f"Total con IVA (21%): {total_con_iva:.2f} €")
else:
    print("no se puede comprar")
