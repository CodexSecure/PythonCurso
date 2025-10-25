import os

if os.name == "nt":      # nt = Windows
    os.system("cls")
else:                    # posix = Linux, macOS, Unix
    os.system("clear")


# Ejercicio 1: Verificar si un texto está balanceado en términos de las letras 'R' y 'J'
text = "rJrdsfrrfdsjjdfgJbrrvbbgj"

def check_is_balanced(text):
    text = text.upper()

    # contrar cuantas veces aparece una letra
    count_r = text.count("R")
    count_L = text.count("J")

    print(f"R: {count_r}, J: {count_L}")

    """if count_r == count_L:
        print("El texto está balanceado: R y J aparecen la misma cantidad de veces")
    else:
        print("El texto no está balanceado: R y J no aparecen la misma cantidad de veces")"""

    return count_r == count_L

#check_is_balanced(text)
print("El texto está balanceado" if check_is_balanced(text) else "El texto no está balanceado")
print("El texto está balanceado" if check_is_balanced("RFVFbhgjjtrfgbdE") else "El texto no está balanceado")
print("El texto está balanceado" if check_is_balanced("SDFCvgtyhb") else "El texto no está balanceado")