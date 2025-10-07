import pandas as pd
import os

# Ruta al archivo original
input_file = r"C:\Users\fidel\Desktop\PythonCurso\Dividir\tickets.csv"

# Carpeta de salida
output_dir = r"C:\Users\fidel\Desktop\PythonCurso\Dividir\salida"
os.makedirs(output_dir, exist_ok=True)  # crea la carpeta si no existe

# Número de filas por archivo
rows_per_file = 25

# Contador de partes
part = 1

# Dividir en chunks y guardar en la carpeta salida
for chunk in pd.read_csv(input_file, chunksize=rows_per_file, encoding="utf-8"):
    output_file = os.path.join(output_dir, f"tickets_part_{part}.csv")
    chunk.to_csv(output_file, index=False)
    print(f"Archivo creado: {output_file} con {len(chunk)} filas")
    part += 1

print("✅ División completada. Archivos guardados en:", output_dir)
