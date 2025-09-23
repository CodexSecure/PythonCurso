# -------------------------------
# SET (mutable)
# -------------------------------
mi_set = {"apple", "banana", "cherry"}
print("SET original:", mi_set)

# Se puede modificar
mi_set.add("mango")         # agregar
mi_set.remove("banana")     # eliminar
print("SET modificado:", mi_set)


# -------------------------------
# FROZENSET (inmutable)
# -------------------------------
mi_frozenset = frozenset({"apple", "banana", "cherry"})
print("\nFROZENSET original:", mi_frozenset)

# ❌ No se puede modificar
# mi_frozenset.add("mango")      # Error
# mi_frozenset.remove("banana")  # Error

# ✅ Pero se puede usar en operaciones de conjuntos
otro = {"banana", "kiwi"}
print("Unión:", mi_frozenset | otro)        # unión
print("Intersección:", mi_frozenset & otro) # intersección

# ✅ También se puede usar como clave en un diccionario
diccionario = {mi_frozenset: "frutas congeladas"}
print("Diccionario con frozenset:", diccionario)
