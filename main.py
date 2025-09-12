# Lista inicial con los dos primeros números de la sucesión
fibonacci = [0, 1]

# Calculamos del índice 2 al 49 (total 50 números)
for i in range(2, 50):
    # Cada nuevo número es la suma de los dos anteriores
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

# Recorremos la lista e imprimimos índice y valor
for index, value in enumerate(fibonacci):
    print(f"{index}: {value}")