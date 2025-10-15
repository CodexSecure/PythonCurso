"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
 """
def son_anagramas(palabra1: str, palabra2: str) -> bool:
    # Si son exactamente iguales, no son anagramas
    if palabra1 == palabra2:
        return False

    # Ordenamos ambas palabras en minúsculas
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

# Ejemplo
print(son_anagramas("roma", "amor"))  # True
print(son_anagramas("roma", "roma"))  # False